"""
=============================================================================
===================라인 색상 검출===라인 색상 검출===========================
===============================================================================
"""
def line_Red_Detection():
    cnt = 0
    gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
    gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)
    time.sleep(1)
    while not cnt == 15:
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        cnt += 1
        if list_Num[2] != 0 and cnt >= 10:
            #print ('red line')
            return 1
    #return 0


def line_Green_Detection():
    cnt = 0
    gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
    gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_green)
    #media_ctrl.zoom_value_update(4)
    #media_ctrl.exposure_value_update(rm_define.exposure_value_small)
    time.sleep(1)
    while not cnt == 15:
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        cnt += 1
        if list_Num[2] != 0 and cnt >= 10:
            #print ('green line')
            return 2
    #return 0


def line_Blue_Detection():
    cnt = 0
    gimbal_ctrl.set_rotate_speed(20) #짐벌 속력
    gimbal_ctrl.pitch_ctrl(-20) #음수 -> 아래로 | 양수 -> 위로
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    time.sleep(1) 
    while not cnt == 15:
        list_Num = RmList(vision_ctrl.get_line_detection_info())
        cnt += 1
        if list_Num[2] != 0 and cnt >= 10:
            #print ('blue line')
            return 3
    #return 0


"""
===============================================================================
===================라인 색상 검출===라인 색상 검출===============================
===============================================================================
"""


"""
===============================================================================
=====================라인 따라가기===라인 따라가기===============================
===============================================================================
"""
def line_Follow():
    line = RmList()
    V = 0.2  
    gimbal_ctrl.pitch_ctrl(-20) 
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow) 
    media_ctrl.exposure_value_update(rm_define.exposure_value_large) 
    vision_ctrl.enable_detection(rm_define.vision_detection_line) 
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue) 
    line = RmList(vision_ctrl.get_line_detection_info()) 
    cnt = 0
    while not cnt == 1:
        if len(line) >= 22:    
            if line[2] == 1:
                cnt = 1
                chassis_ctrl.stop()
            t = line[5]      
            if line[3] >= 0.6:   
                dy = line[3] - 0.77   
            else:
                dy = line[3] - 0.5     
            chassis_ctrl.move_with_speed(V,3 * dy,t * 2) 
        else:
            chassis_ctrl.stop()
        line=RmList(vision_ctrl.get_line_detection_info())
"""
===============================================================================
=====================라인 따라가기===라인 따라가기===============================
===============================================================================
"""

"""
===============================================================================
=====================라인 트랙킹===라인 트랙킹===============================
===============================================================================
"""

def line_Tracking_v3(set_speed, set_color):
    pid_pid = rm_ctrl.PIDCtrl()
    pid_cpst = rm_ctrl.PIDCtrl()
    pid_speed = rm_ctrl.PIDCtrl()
    pid_pitch = rm_ctrl.PIDCtrl()
    pid_Follow_Line = rm_ctrl.PIDCtrl()
    list_LineList = RmList()
    list_MarkerList = RmList()
    list_k = RmList()
    pid_Follow_Line = rm_ctrl.PIDCtrl()
    gimbal_ctrl.set_follow_chassis_offset(0)
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,20)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    #vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    if set_color == 'red':
        vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)
    if set_color == 'green':
        vision_ctrl.line_follow_color_set(rm_define.line_follow_color_green)
    if set_color == 'blue':
        vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    pid_Follow_Line.set_ctrl_params(330,0,28)
    time.sleep(0.5)
    cnt = 0
    while not cnt == 1:
        list_LineList=RmList(vision_ctrl.get_line_detection_info())
        if len(list_LineList) == 42: #라인 인식
            #time.sleep(0.5)
            if list_LineList[2] >= 1: #싱글 라인
                
                robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
                variable_x = list_LineList[19]
                pid_Follow_Line.set_error(variable_x - 0.5)
                gimbal_ctrl.rotate_with_speed(pid_Follow_Line.get_output(),0)
                chassis_ctrl.set_trans_speed(set_speed)
                chassis_ctrl.move(0)
                if list_LineList[2] == 2:
                    print('T line')
                    cnt = 1

                if list_LineList[2] == 3:
                    print('+ line')
                    cnt = 1

        else:
            print('no line')
            gimbal_ctrl.rotate_with_speed(0,0)
            cnt = 1
"""
===============================================================================
=====================라인 트랙킹===라인 트랙킹===============================
===============================================================================
"""

"""
===============================================================================
=====================강제 이동===강제 이동===============================
===============================================================================
"""

def move_Axis(set_speed, set_angle, set_distance, set_sleep):
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_trans_speed(set_speed)
    chassis_ctrl.move_with_distance(set_angle, set_distance)
    time.sleep(set_sleep)

"""
===============================================================================
=====================강제 이동===강제 이동===============================
===============================================================================
"""

"""
===============================================================================
=====================회전===회전===============================
===============================================================================
"""
def move_Turn(set_speed, set_angle, set_dir, set_sleep):
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_rotate_speed(set_speed)
    if set_dir == 'left':
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, set_angle)
        time.sleep(set_sleep)
    elif set_dir == 'right':
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, set_angle)
        time.sleep(set_sleep)
"""
===============================================================================
=====================회전===회전===============================
===============================================================================
"""

"""
===============================================================================
=====================번호 검출===번호 검출===============================
===============================================================================
"""

def number_Detection(set_distance):
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(set_distance)
    while True:
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_zero):
            return 0
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one):
            return 1
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two):
            return 2
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three):
            return 3
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_four):
            return 4
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_five):
            return 5
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_six):
            return 6
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_seven):
            return 7
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_eight):
            return 8
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_nine):
            return 9
"""
===============================================================================
=====================번호 검출===번호 검출===============================
===============================================================================
"""

"""
===============================================================================
=====================총 쏘기===총 쏘기===============================
===============================================================================
"""

list_MarkerList_2 = RmList()
list_ShootList = RmList()
list_MarkerList = RmList()
list_n = RmList()
variable_StartFlag = 0
variable_i = 0
variable_Yaw = 0
variable_Pitch = 0
variable_Position = 0
variable_Error_x = 0
variable_Error_y = 0
variable_ID = 0
variable_Post = 0
pid_X = rm_ctrl.PIDCtrl()
pid_Y = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()

def user_defined_Shoot():
    global variable_StartFlag
    global variable_i
    global variable_Yaw
    global variable_Pitch
    global variable_Position
    global variable_Error_x
    global variable_Error_y
    global variable_ID
    global variable_Post
    global list_MarkerList_2
    global list_ShootList
    global list_MarkerList
    global list_n
    global pid_X
    global pid_Y
    global pid_Yaw
    global pid_Pitch
    pid_Yaw.set_ctrl_params(110,0,10)
    pid_Pitch.set_ctrl_params(95,0,5)
    while not len(list_ShootList) == 0:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info()) #마커 타겟 정보 입력
        if (list_ShootList[1] in (list_MarkerList)): #타겟 안에 쏠 목표가 있는가
            variable_Position = (list_MarkerList.index(list_ShootList[1])) #타겟 설정
            variable_ID = list_MarkerList[variable_Position] #타겟 저장
            variable_Error_x = list_MarkerList[variable_Position + 1] - 0.5 #목표 조준
            variable_Error_y = 0.5 - list_MarkerList[variable_Position + 2] #목표 조준
            pid_Yaw.set_error(variable_Error_x) #목표 조준
            pid_Pitch.set_error(variable_Error_y) #목표 조준
            gimbal_ctrl.rotate_with_speed(pid_Yaw.get_output(),pid_Pitch.get_output()) # (속도 설정)목표 조준
            variable_Post = 0.01
            if abs(variable_Error_x) <= variable_Post and abs(variable_Error_y) <= variable_Post: #정중앙이면
                list_ShootList.pop(1) #첫 번째 목표 제거
                media_ctrl.play_sound(rm_define.media_sound_shoot)
                gun_ctrl.fire_once() #목표 제거
        else:
            gimbal_ctrl.rotate_with_speed(0,0)
            list_ShootList.insert(1, list_ShootList[len(list_ShootList)])
            list_ShootList.pop(len(list_ShootList)) #종료

def user_defined_Save():
    global variable_StartFlag
    global variable_i
    global variable_Yaw
    global variable_Pitch
    global variable_Position
    global variable_Error_x
    global variable_Error_y
    global variable_ID
    global variable_Post
    global list_MarkerList_2
    global list_ShootList
    global list_MarkerList
    global list_n
    global pid_X
    global pid_Y
    global pid_Yaw
    global pid_Pitch
    media_ctrl.play_sound(rm_define.media_sound_scanning,wait_for_complete_flag=True) #스캔 전 사운드
    variable_StartFlag = 0
    list_MarkerList.append(0)
    while not variable_StartFlag == 1: # 1이 아닐 때 까지 반복
        for count in range(20): #20번 반복 
            list_MarkerList_2=RmList(vision_ctrl.get_marker_detection_info()) #list_MarkerList_2에 마커 정보 입력
            if list_MarkerList_2[1] > list_MarkerList[1]: # 번호 인식이 된 경우
                list_MarkerList=RmList(list_MarkerList_2) # MarkerList에 번호 저장
            time.sleep(0.1)
        if list_MarkerList[1] >= 1: #저장된 마커의 개수가 1개 보다 크거나 같으면
            variable_i = 2 
            for count in range(int(list_MarkerList[1])): #마커의 개수만큼 반복
                list_ShootList.append(list_MarkerList[variable_i]) #ShootList에 마커 숫자 저장
                variable_i = variable_i + 5 #다음 마커 숫자 읽어옴
            print('save')
            variable_StartFlag = 1 #종료

"""
===============================================================================
=====================총 쏘기===총 쏘기===============================
===============================================================================
"""

def line_Check():
    red_Result = line_Red_Detection()
    print(red_Result)
    green_Result = line_Green_Detection()
    print(green_Result)
    blue_Result = line_Blue_Detection()
    print(blue_Result)

    if red_Result is None:
        red_Result = 0
    if green_Result is None:
        green_Result = 0
    if blue_Result is None:
        blue_Result = 0

    result = red_Result + green_Result + blue_Result

    return result

def start():
    global variable_i
    global variable_Yaw
    global variable_Pitch
    global variable_Position
    global variable_Error_x
    global variable_Error_y
    global variable_ID
    global variable_Post
    global list_MarkerList_2
    global list_ShootList
    global list_MarkerList
    global list_n
    global pid_X
    global pid_Y
    global pid_Yaw
    global pid_Pitch
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)

    #move_Axis(0.3, 90, 0.5, 0.5)
    #line_Follow()
    #move_Axis(0.3, 0, 0.35, 0.5)

    #result = line_Check()

    #user_defined_Save()

    #move_Turn(300, 90, 'right', 0.5)
    #move_Axis(0.3, -40, 1, 0.5)
    result = 1
    

    cnt = 0
    while not cnt == 1:
        second_result = line_Check()
        print (second_result)
        if result == second_result:
            if result == 1:
                line_Tracking_v3(0.3, 'red')
                cnt = 1

            if result == 2:
                line_Tracking_v3(0.3, 'green')
                cnt = 1

            if result == 3:
                line_Tracking_v3(0.3, 'blue')
                cnt = 1

        else:
            move_Axis(0.3,90,0.8,0.5)    

    """총쏘기 메인 부분"""
    """global variable_StartFlag
    global variable_i
    global variable_Yaw
    global variable_Pitch
    global variable_Position
    global variable_Error_x
    global variable_Error_y
    global variable_ID
    global variable_Post
    global list_MarkerList_2
    global list_ShootList
    global list_MarkerList
    global list_n
    global pid_X
    global pid_Y
    global pid_Yaw
    global pid_Pitch
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.set_rotate_speed(180)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,90)
    user_defined_Save()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    user_defined_Shoot()
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    led_ctrl.gun_led_on()"""
    """총쏘기 메인 부분"""
