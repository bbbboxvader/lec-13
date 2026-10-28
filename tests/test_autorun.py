from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pico2d import SDL_KEYDOWN, SDL_KEYUP, SDLK_LEFT, SDLK_RIGHT, SDLK_SPACE, SDLK_a
from auto_run import AutoRun
from boy import Boy


class AutoRunTests(unittest.TestCase):
    def setUp(self):
        self.now = 100.0
        self.image = Mock()
        for target, kwargs in [
            ('boy.monotonic', {'side_effect': lambda: self.now}),
            ('auto_run.monotonic', {'side_effect': lambda: self.now}),
            ('boy.get_canvas_width', {'return_value': 800}),
            ('auto_run.get_canvas_width', {'return_value': 800}),
            ('boy.load_image', {'return_value': self.image}),
        ]:
            patcher = patch(target, **kwargs)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.boy = Boy()

    def key(self, code, down=True, repeat=0):
        self.boy.handle_event(SimpleNamespace(
            type=SDL_KEYDOWN if down else SDL_KEYUP, key=code, repeat=repeat,
        ))

    def step(self, seconds):
        self.now += seconds
        self.boy.update()

    def test_a_enters_real_autorun_class_from_idle(self):
        self.key(SDLK_a)
        self.assertIsInstance(self.boy.auto_run, AutoRun)
        self.assertEqual(self.boy.state, 'AUTO_RUN')

    def test_moves_without_further_input_at_double_run_speed(self):
        self.key(SDLK_a)
        self.step(0.5)
        self.assertEqual(self.boy.x, 600)
        self.assertEqual(self.boy.auto_run.SPEED_MULTIPLIER, 2)

    def test_uses_running_animation(self):
        self.key(SDLK_a)
        self.step(0.1)
        self.assertAlmostEqual(self.boy.frame, 1)
        self.boy.draw()
        self.assertEqual(self.image.clip_draw.call_args.args[1], 100)

    def test_grows_to_150_pixels_and_keeps_feet_on_ground(self):
        self.key(SDLK_a)
        self.boy.draw()
        args = self.image.clip_draw.call_args.args
        self.assertEqual(args[-2:], (150, 150))
        self.assertEqual(args[5] - args[-1] / 2, self.boy.y - 50)

    def test_entry_keeps_enlarged_sprite_inside_screen(self):
        for x, expected in [(50, 75), (750, 725)]:
            with self.subTest(x=x):
                self.boy = Boy()
                self.boy.x = x
                self.key(SDLK_a)
                self.assertEqual(self.boy.x, expected)

    def test_right_edge_bounces_and_preserves_distance(self):
        self.boy.x = 700
        self.key(SDLK_a)
        self.step(0.1)
        self.assertAlmostEqual(self.boy.x, 710)
        self.assertEqual(self.boy.face_dir, -1)

    def test_left_edge_bounces_and_preserves_distance(self):
        self.boy.x, self.boy.face_dir = 100, -1
        self.key(SDLK_a)
        self.step(0.1)
        self.assertAlmostEqual(self.boy.x, 90)
        self.assertEqual(self.boy.face_dir, 1)

    def test_long_frame_handles_multiple_bounces(self):
        self.key(SDLK_a)
        self.step(4.0)
        self.assertEqual(self.boy.state, 'AUTO_RUN')
        self.assertEqual((self.boy.x, self.boy.face_dir), (700, 1))

    def test_timeout_occurs_at_five_seconds_and_restores_idle(self):
        self.key(SDLK_a)
        self.step(4.999)
        self.assertEqual(self.boy.state, 'AUTO_RUN')
        self.now = 105.0
        self.boy.update()
        self.assertEqual(self.boy.state, 'IDLE')
        self.assertEqual(self.boy.idle_started_at, 105)
        self.assertIsNone(self.boy.auto_run.started_at)
        self.boy.draw()
        self.assertEqual(len(self.image.clip_draw.call_args.args), 6)








if __name__ == '__main__':
    unittest.main()
