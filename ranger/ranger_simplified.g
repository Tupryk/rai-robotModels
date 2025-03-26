ranger_world: { X: [0, 0., .5]},
ranger_joint(ranger_world) { joint: transXYPhi }
ranger(ranger_joint): { Q: [0, 0, 0, 0.000796327, 1, 0, 0], shape: mesh, color: [0.792157, 0.819608, 0.933333, 1], mesh: <meshes/ranger_mini3.ply>, visual: True }
livox_point_cloud(ranger): { X: [.27, 0., .57], shape: marker, color: [0., 0., 1., 1], size:[.1], visual: True }
