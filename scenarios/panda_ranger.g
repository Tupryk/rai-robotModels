Include: <../ranger/ranger.g>

## pandas
Prefix: "l_"
Include: <../panda/panda.g>
#Prefix: "r_"
#Include: <../panda/panda.g>
Prefix: False

## position them on the table
Edit l_panda_base (ranger_base_link): { Q: "t(-.25 .0 .04) d(180 0 0 1)", joint: none, multibody: false }
#Edit r_panda_base (ranger_base_link): { Q: "t( .22 .05 .02) d(0 0 0 1)", joint: rigid }

## control box
controlBox (ranger_base_link){ Q: [.15 0 .1], shape: ssBox, size: [.35 .45 .16 .01], color: [.1] }

## cameras

cameraPillar_l (controlBox){ Q: [.185 -.205 .39], shape: ssBox, size: [.02 .04 .94 .001], color: [.75] }
cameraPillar_r (controlBox){ Q: [.185 .205 .39], shape: ssBox, size: [.02 .04 .94 .001], color: [.75] }

cam_l(cameraPillar_l): {
 Q: "t(-0.02 0.0 0.45) d(-120 0 1 0) d(90 0 0 1)",
 shape: marker, size: [.1],
 focalLength: 0.895, width: 640, height: 360, zRange: [.5, 100]
}

cam_r(cameraPillar_r): {
 Q: "t(-0.02 0.0 0.45) d(-120 0 1 0) d(90 0 0 1)",
 shape: marker, size: [.1],
 focalLength: 0.895, width: 640, height: 360, zRange: [.5, 100]
}
