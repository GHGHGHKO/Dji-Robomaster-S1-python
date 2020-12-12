def move_Axis(set_speed, set_angle, set_distance, set_sleep):
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_trans_speed(set_speed)
    chassis_ctrl.move_with_distance(set_angle, set_distance)
    time.sleep(set_sleep)