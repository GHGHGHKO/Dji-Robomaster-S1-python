def turn_Func(set_speed, set_rotate, set_angle, set_sleep):
    while True:
        chassis_ctrl.set_rotate_speed(set_speed)
        if set_rotate == 1:
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, set_angle)
            time.sleep(set_sleep)
            return
        else:
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, set_angle)
            time.sleep(set_sleep)
            return