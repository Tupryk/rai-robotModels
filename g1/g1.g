## create standard base frame before including

g1_base: { X:[0, 0, .79], multibody: true, multibody_fixedBase: false }
Include: <g1_clean.g>
Edit pelvis(g1_base): {}
