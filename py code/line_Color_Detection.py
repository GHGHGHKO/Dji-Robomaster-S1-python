def line_Color_Detection():
	gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
	gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
	vision_ctrl.enable_detection(rm_define.vision_detection_line)
	time.sleep(0.5)

	while True:
		vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        if list_Num[2] != 0:
        	print ('red line')

		vision_ctrl.line_follow_color_set(rm_define.line_follow_color_green)
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        if list_Num[2] != 0:
        	print ('green line')

		vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
        list_Num = RmList(vision_ctrl.get_line_detection_info())

        if list_Num[2] != 0:
        	print ('blue line')

def line_Red_Detection():
	gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
	gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
	vision_ctrl.enable_detection(rm_define.vision_detection_line)

	while True:
		vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        if list_Num[2] != 0:
        	print ('red line')

def line_Green_Detection():
	gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
	gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
	vision_ctrl.enable_detection(rm_define.vision_detection_line)

	while True:
		vision_ctrl.line_follow_color_set(rm_define.line_follow_color_Green)
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        if list_Num[2] != 0:
        	print ('green line')

def line_Blue_Detection():
	gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
	gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
	vision_ctrl.enable_detection(rm_define.vision_detection_line)

	while True:
		vision_ctrl.line_follow_color_set(rm_define.line_follow_color_Blue)
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        if list_Num[2] != 0:
        	print ('blue line')


def start():
    line_Red_Detection()
    line_Green_Detection()
    line_Blue_Detection()