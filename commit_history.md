# Character controller: 15 local commits

Branch: `refs/heads/main`
Base: `6d93e4e59dab22297c9c61d09cd3581362b5c40c`
HEAD: `d2ca5d630d78e65366d8a13775ee14c82b2b265f`

Working files and unrelated modifications were preserved. No push was performed.

1. `b77a3b4` build: declare pico2d and transitions dependencies
2. `f1052f4` feat: add reusable Grass game object
3. `65853fe` feat: add Boy object with repeating idle animation
4. `6ddcf51` feat: assemble grass and boy in the game loop
5. `9e59a34` feat: model IDLE with transitions Machine
6. `702c2bf` feat: track IDLE duration with a monotonic timer
7. `dbc9c45` feat: enter SLEEP after five idle seconds and draw a sleeping pose
8. `a52dcac` feat: route keyboard events and wake SLEEP with Space
9. `294e074` fix: animate at ten frames per second using elapsed time
10. `6bd8453` feat: add one RUN state with arrow input and directional running sprites
11. `4d0b2b0` fix: keep the running sprite inside the screen bounds
12. `53138b8` fix: keep running while either direction key remains held
13. `5aee6f2` fix: ignore key repeat when choosing the latest direction
14. `031f7cc` feat: allow arrow input to transition directly from SLEEP to RUN
15. `d2ca5d6` docs: describe IDLE SLEEP RUN behavior and the target state diagram
