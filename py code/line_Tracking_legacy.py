#라인 따라가는 코드
pid_Test = rm_ctrl.PIDCtrl()
list_LineList = RmList()
variable_X = 0
variable_Turned = 0
variable_Turn2 = 0

def start():
    global variable_X
    global list_LineList
    global pid_Test
    variable_Turned = 0
    variable_Turn2 = -5
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    pid_Test.set_ctrl_params(330,0,28)# 330, 0, 28
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 127, 70, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 161, 255, 69, rm_define.effect_always_on)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    gimbal_ctrl.set_rotate_speed(10)
    gimbal_ctrl.pitch_ctrl(-20)
    while True:
        list_LineList=RmList(vision_ctrl.get_line_detection_info())
        if len(list_LineList) == 42:
            if list_LineList[2] <= 1:
                variable_X = list_LineList[19]
                pid_Test.set_error(variable_X - 0.5)
                gimbal_ctrl.rotate_with_speed(pid_Test.get_output(),0)
                chassis_ctrl.set_trans_speed(0.3)
                chassis_ctrl.move(0)
                time.sleep(0.05)
        else:
            chassis_ctrl.stop()
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
            led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
            gimbal_ctrl.rotate_with_speed(-20,0) #인식을 못했을경우 회전
            time.sleep(2)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 127, 70, rm_define.effect_flash)
            led_ctrl.set_top_led(rm_define.armor_top_all, 161, 255, 69, rm_define.effect_always_on) 