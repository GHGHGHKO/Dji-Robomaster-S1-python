def move_Turn(set_speed, set_angle, set_dir):
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_rotate_speed(set_speed)
    if set_dir == 'left':
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, set_angle)
    elif set_dir == 'right':
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, set_angle)

def start():
    move_Turn(300, 360, 'left')