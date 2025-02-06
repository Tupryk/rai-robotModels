from lxml import etree


def writeShape(link):
    elem = link.find('origin')
    if elem is not None:
        xyz = elem.attrib.get('xyz')
        rpy = elem.attrib.get('rpy')
        if rpy=='0 0 0':
            rpy=None
        if xyz=='0 0 0':
            xyz=None
        if xyz is not None and rpy is not None:
            print(' rel: "t(%s) E(%s)",' % (xyz, rpy), end='')
        else:
            if rpy is not None:
                print(' rel: "E(%s)",' % (rpy), end='')
            if xyz is not None:
                print(' rel: [%s],' % (xyz), end='')

    elem = link.find('geometry/mesh')
    if elem is not None:
        print(' mesh: <%s>,' % filename, end='')
        if elem.find('scale') is not None:
            print(' meshscale: [%s],' % elem.attrib['scale'], end='')

    elem = link.find('material/color')
    if elem is not None:
        print(' color: [%s],' % elem.attrib['rgba'], end='')


if __name__ == "__main__":

    inFile = "fixtures/microwaves/pack_1/model.xml"
    xmlData = etree.parse(inFile)

    links = xmlData.findall('./mujoco')
    for link in links:
        name = link.attrib['name']
        print('%s: {' % name, end='')

        print(f' mass: {1.},', end='')

        print('}') # end of body

        # visual shape
        for visual in link.findall('visual'):
            print('%s_0 (%s): {' % (name, name), end='')
            writeShape(visual)
            print(' visual: true }') # end of shape

    # joints = xmlData.findall('/joint')
    # for joint in joints:
    #     name = joint.attrib['name']
    #     if joint.find('child') is not None:

    #         parent = joint.find('parent').attrib['link']

    #         # add an origin frame as pre frame?
    #         elem = joint.find('origin')
    #         if elem is not None:
    #             xyz = elem.attrib.get('xyz')
    #             rpy = elem.attrib.get('rpy')
    #             if rpy=='0 0 0':
    #                 rpy=None
    #             if xyz=='0 0 0':
    #                 xyz=None
    #             if xyz is not None and rpy is not None:
    #                 print('%s (%s): { Q: "t(%s) E(%s)" }' % (name+'_origin', parent, xyz, rpy))
    #                 parent = name+'_origin'
    #             elif rpy is not None:
    #                 print('%s (%s): { Q: "E(%s)" }' % (name+'_origin', parent, rpy))
    #                 parent = name+'_origin'
    #             elif xyz is not None:
    #                 print('%s (%s): { Q: [%s] }' % (name+'_origin', parent, xyz))
    #                 parent = name+'_origin'

    #         #print('%s (%s): {' % (name, parent), end='')
    #         print('%s (%s %s): {' % (name, parent, joint.find('child').attrib['link']), end='')

    #         # figure out joint type
    #         att = joint.attrib.get('type')
            
    #         if att in ['revolute', 'continuous']:
    #             elem = joint.find('axis')
    #             if elem is not None:
    #                 axis = elem.attrib['xyz']
    #                 if axis=='1 0 0':
    #                     print(' joint: hingeX,', end='')
    #                 elif axis=='0 1 0':
    #                     print(' joint: hingeY,', end='')
    #                 elif axis=='0 0 1':
    #                     print(' joint: hingeZ,', end='')
    #                 elif axis=='0 0 -1':
    #                     print(' joint: hingeZ, joint_scale: -1,', end='')
    #                 else:
    #                     raise Exception('CAN ONLY PROCESS X Y Z prismatic joints, not', axis)
    #             else:
    #                 print(' joint: hingeX,', end='')
                    
    #         if att == 'prismatic':
    #             elem = joint.find('axis')
    #             if elem is not None:
    #                 axis = elem.attrib['xyz']
    #                 if axis=='1 0 0':
    #                     print(' joint: transX,', end='')
    #                 elif axis=='0 1 0':
    #                     print(' joint: transY,', end='')
    #                 elif axis=='0 -1 0':
    #                     print(' joint: transY, joint_scale: -1,', end='')
    #                 elif axis=='0 0 1':
    #                     print(' joint: transZ,', end='')
    #                 elif axis=='0 0 -1':
    #                     print(' joint: transZ, joint_scale: -1,', end='')
    #                 else:
    #                     raise Exception('CAN ONLY PROCESS X Y Z prismatic joints, not', axis)
    #             else:
    #                 print(' joint: transX,', end='')
                    
    #         if att == 'fixed':
    #             print(' joint: rigid,', end='')

    #         elem = joint.find('mimic')
    #         if elem is not None:
    #             print(' mimic: %s,' % elem.attrib['joint'], end='')

    #         elem = joint.find('limit')
    #         if elem is not None:
    #             lo = elem.attrib.get('lower')
    #             up = elem.attrib.get('upper')
    #             eff = elem.attrib.get('effort')
    #             vel = elem.attrib.get('velocity')
    #             if eff=='0':
    #                 eff=None
    #             if vel=='0':
    #                 vel=None
    #             if lo is not None:
    #                 print(' limits: [%s %s],' % (lo, up), end='')
    #             if vel is not None:
    #                 print(' ctrl_limits: [%s -1 %s],' % (vel, eff), end='') #the 2nd value is an acceleration limit
    #         else:
    #             elem = joint.find('safety_controller')
    #             if elem is not None:
    #                 lo = elem.attrib.get('soft_lower_limit')
    #                 up = elem.attrib.get('soft_upper_limit')
    #                 if lo is not None:
    #                     print(' limits: [%s %s],' % (lo, up), end='')

    #         print('}')
