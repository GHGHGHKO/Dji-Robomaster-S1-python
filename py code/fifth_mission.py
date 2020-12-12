import time


sum_List = []
dup_Num = 0
sort_Dic = {}
dic_insert_null = 2
init_angle = 0
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
   
def line_Center(set_time):
    line = RmList()
    V = 0.0
    gimbal_ctrl.pitch_ctrl(-20) 
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.set_follow_chassis_offset(0)
    
    #robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow) 
    chassis_ctrl.set_follow_gimbal_offset(0)
    vision_ctrl.enable_detection(rm_define.vision_detection_line) 
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red) 
    line = RmList(vision_ctrl.get_line_detection_info()) 
    cnt = 0
    start = time.time()
    while not cnt == 1 and (time.time() - start) <= set_time:
        print('time :', time.time() - start)
        if len(line) >= 22:    
            """if line[2] != 1:
                cnt = 1
                print('stop because', line[2])
                chassis_ctrl.stop()"""

            t = line[5]      
            print('t', t)
            if line[3] >= 0.0:   
                dy = line[3] - 0.5   

            else:
                dy = line[3] + 0.4     
            chassis_ctrl.move_with_speed(V,3 * dy,t * 2) 
        else:
            chassis_ctrl.stop()
        line=RmList(vision_ctrl.get_line_detection_info())
        #gimbal_ctrl.set_follow_chassis_offset(0)
    chassis_ctrl.stop()

pid_x = rm_ctrl.PIDCtrl()
pid_y = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()
variable_X = 0
variable_Y = 0
variable_Post = 0
list_LineList = RmList()

pid_x = rm_ctrl.PIDCtrl()
pid_y = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()
variable_X = 0
variable_Y = 0
variable_Post = 0
list_LineList = RmList()

def line_Center_v2(set_time):
    line = RmList()
    V = 0.0  
    gimbal_ctrl.pitch_ctrl(-20) 
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow) 
    media_ctrl.exposure_value_update(rm_define.exposure_value_large) 
    vision_ctrl.enable_detection(rm_define.vision_detection_line) 
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue) 
    line = RmList(vision_ctrl.get_line_detection_info()) 
    cnt = 0
    start = time.time()
    while not cnt == 1 and (time.time() - start) <= set_time:
        if len(line) >= 22:    
            if line[2] > 1:
                cnt = 1
                print('2 line upper')
            t = line[5]      
            if line[3] >= 0.0:   
                dy = line[3] - 0.5   
            else:
                dy = line[3] + 0.5     
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

def line_Tracking_v4_select(set_speed, set_color, set_exit, set_time = 9999):
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
    #robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
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
    start = time.time()
    while not cnt == 1:
        
        list_LineList=RmList(vision_ctrl.get_line_detection_info())
        if len(list_LineList) == 42: #라인 인식
            #time.sleep(0.5)
            if list_LineList[2] >= 1: #싱글 라인
                if set_time <= time.time() - start:
                    cnt = 1
                    print('time out')
                    time.sleep(0.5)
                
                #robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
                variable_x = list_LineList[19]
                pid_Follow_Line.set_error(variable_x - 0.5)
                gimbal_ctrl.rotate_with_speed(pid_Follow_Line.get_output(),0)
                chassis_ctrl.set_trans_speed(set_speed)
                chassis_ctrl.move(0)

                if list_LineList[2] == 2 and set_exit == 2:
                    print('T line')
                    cnt = 1
                    #gimbal_ctrl.rotate_with_speed(0,0)
                    #chassis_ctrl.stop()
                    time.sleep(0.5)

                if list_LineList[2] == 3  and set_exit == 3:
                    print('+ line')
                    cnt = 1
                    #gimbal_ctrl.rotate_with_speed(0,0)
                    #chassis_ctrl.stop()
                    time.sleep(0.5)
        else:
            print('no line')
            gimbal_ctrl.rotate_with_speed(0,0)
            chassis_ctrl.stop()
            cnt = 1
            time.sleep(0.5)
    #robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.rotate_with_speed(0,0)
    chassis_ctrl.stop()
    gimbal_ctrl.set_follow_chassis_offset(0)
"""
===============================================================================
=====================라인 트랙킹===라인 트랙킹===============================
===============================================================================
"""

def line_Tracking_With_Marker(set_speed, set_color, set_exit, set_time = 9999):
    global dup_Num
    detected_Num = []
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
    #robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,20)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.set_marker_detection_distance(1.5)
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
    start = time.time()
    while not cnt == 1:
        marker = RmList(vision_ctrl.get_marker_detection_info()) # called vision marker
        list_LineList=RmList(vision_ctrl.get_line_detection_info())
        
        if marker[1] == 0:
            marker = [0, 0, 0, 0.5]

        elif marker[2] > 0:
            if marker[2] not in detected_Num and marker[2] != 47:
                detected_Num.append(marker[2])

        if len(list_LineList) == 42: #라인 인식
            #time.sleep(0.5)
            if list_LineList[2] >= 1: #싱글 라인
                if set_time <= time.time() - start:
                    cnt = 1
                    print('time out')
                    time.sleep(0.5)
                
                #robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
                variable_x = list_LineList[19]
                pid_Follow_Line.set_error(variable_x - 0.5)
                gimbal_ctrl.rotate_with_speed(pid_Follow_Line.get_output(),0)
                chassis_ctrl.set_trans_speed(set_speed)
                chassis_ctrl.move(0)

                if list_LineList[2] == 2 and set_exit == 2:
                    print('T line')
                    cnt = 1
                    #gimbal_ctrl.rotate_with_speed(0,0)
                    #chassis_ctrl.stop()
                    time.sleep(0.5)

                if list_LineList[2] == 3  and set_exit == 3:
                    print('+ line')
                    cnt = 1
                    #gimbal_ctrl.rotate_with_speed(0,0)
                    #chassis_ctrl.stop()
                    time.sleep(0.5)
        else:
            print('no line')
            gimbal_ctrl.rotate_with_speed(0,0)
            chassis_ctrl.stop()
            cnt = 1
            time.sleep(0.5)
    #robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.rotate_with_speed(0,0)
    chassis_ctrl.stop()
    gimbal_ctrl.set_follow_chassis_offset(0)

    return detected_Num



"""
===============================================================================
=====================강제 이동===강제 이동===============================
===============================================================================
"""

def move_Axis(set_speed, set_angle, set_distance, set_sleep):
    #gimbal_ctrl.set_follow_chassis_offset(0)
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    #chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_trans_speed(set_speed)
    chassis_ctrl.move_with_distance(set_angle, set_distance)
    #gimbal_ctrl.rotate_with_speed(0,0)
    #chassis_ctrl.stop()
    #gimbal_ctrl.set_follow_chassis_offset(0)
    time.sleep(set_sleep)

def move_Axis_Stop_Marker(set_speed, set_marker, set_sleep):
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(0.5)
    chassis_ctrl.move_with_speed(set_speed, 0, 0)
    gimbal_ctrl.pitch_ctrl(-20)
    cnt = 0

    while not cnt == 1:
        marker = RmList(vision_ctrl.get_marker_detection_info())
        print(marker)
        if set_marker in marker:
            cnt = 1

    chassis_ctrl.stop()
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
    gimbal_ctrl.set_follow_chassis_offset(0)
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

def move_Turn_gimbal(set_speed, set_angle, set_sleep):
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    gimbal_ctrl.set_rotate_speed(set_speed)
    gimbal_ctrl.yaw_ctrl(set_angle)
    time.sleep(set_sleep)

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
    time.sleep(1)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    #time.sleep(0.5)
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
                led_ctrl.gun_led_on()
                gun_ctrl.fire_once() #목표 제거
                time.sleep(1)
                led_ctrl.gun_led_off()
                
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
                print(list_ShootList)
            print('save')
            variable_StartFlag = 1 #종료

def user_defined_Save_Modified():
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
    global pid_Pitch"""
    modified_list_MarkerList_2 = RmList()
    modified_list_ShootList = RmList()
    modified_list_MarkerList = RmList()
    modified_list_n = RmList()
    modified_variable_StartFlag = 0
    modified_variable_i = 0
    modified_variable_Yaw = 0
    modified_variable_Pitch = 0
    modified_variable_Position = 0
    modified_variable_Error_x = 0
    modified_variable_Error_y = 0
    modified_variable_ID = 0
    modified_variable_Post = 0
    media_ctrl.play_sound(rm_define.media_sound_scanning,wait_for_complete_flag=True) #스캔 전 사운드
    modified_variable_StartFlag = 0
    modified_list_MarkerList.append(0)
    while not modified_variable_StartFlag == 1: # 1이 아닐 때 까지 반복
        chassis_ctrl.set_wheel_speed(1, 1, 1, 1)
        for count in range(20): #20번 반복 
            modified_list_MarkerList_2=RmList(vision_ctrl.get_marker_detection_info()) #list_MarkerList_2에 마커 정보 입력
            if modified_list_MarkerList_2[1] > modified_list_MarkerList[1]: # 번호 인식이 된 경우
                modified_list_MarkerList=RmList(modified_list_MarkerList_2) # MarkerList에 번호 저장
                time.sleep(0.1)
        if modified_list_MarkerList[1] >= 1: #저장된 마커의 개수가 1개 보다 크거나 같으면
                #variable_i = 2 
            #print('save')
            modified_variable_StartFlag = 1
            return modified_list_MarkerList[2]
    #for count in range(int(list_MarkerList[1])): #마커의 개수만큼 반복
    #    list_ShootList.append(list_MarkerList[variable_i]) #ShootList에 마커 숫자 저장
    #    variable_i = variable_i + 5 #다음 마커 숫자 읽어옴
    #print('save')
    #variable_StartFlag = 1 #종료



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

def init():
    global sight
    #robot_ctrl.set_mode(rm_define.robot_mode_free)
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    gimbal_ctrl.set_rotate_speed(270)
    chassis_ctrl.set_trans_speed(0.5)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    #vision_ctrl.set_marker_detection_distance(0.6)
    #gun_ctrl.set_fire_count(1)
    sight = RmList(media_ctrl.get_sight_bead_position())
    gimbal_ctrl.pitch_ctrl(-20)

def position_x(gimbal_yaw,direction,speed,t):
    global marker
    gimbal_ctrl.yaw_ctrl(gimbal_yaw)
    marker = RmList(vision_ctrl.get_marker_detection_info())
    chassis_ctrl.move_degree_with_speed(speed,direction)
    while marker[1] < 1:
        marker = RmList(vision_ctrl.get_marker_detection_info())
    chassis_ctrl.move_degree_with_speed(0.15,direction)   
    while marker[6] < t:
        marker = RmList(vision_ctrl.get_marker_detection_info())
        while marker[1] < 1:
            marker = RmList(vision_ctrl.get_marker_detection_info())
    chassis_ctrl.stop()

def position_y(gimbal_yaw, direction, speed, set_time):
    global marker
    global dic_insert_null
    cnt = 0
    cnt1 = 0
    gimbal_ctrl.yaw_ctrl(gimbal_yaw)
    #media_ctrl.zoom_value_update(1)
    vision_ctrl.set_marker_detection_distance(0.8)
    #gimbal_ctrl.pitch_ctrl(-7)
    time.sleep(1.5)
    marker = RmList(vision_ctrl.get_marker_detection_info())
    chassis_ctrl.move_degree_with_speed(speed,direction)
    start = time.time()
    while (marker[1] < 1 and (time.time() - start) <= set_time) or (marker[2] in detected_Num): 
        marker = RmList(vision_ctrl.get_marker_detection_info())
        if marker[1] == 0:
            marker = [0, 0, 0, 0.5]
            #print(marker[2])
        #print(time.time() - start)

    #print('y while')

    #while abs(marker[3]-0.5) > 0.05:
    while abs(marker[3]-0.5) > 0.05:
        media_ctrl.zoom_value_update(1)
        vision_ctrl.set_marker_detection_distance(1.5)
        chassis_ctrl.move_degree_with_speed(0.1, direction)
        marker = RmList(vision_ctrl.get_marker_detection_info())
        if cnt == 0:
            media_ctrl.play_sound(rm_define.media_sound_recognize_success)
            detected_Num.append(marker[2])
            #print('detected_Num', detected_Num)
            cnt = 1

        while marker[1] < 1:
            marker = RmList(vision_ctrl.get_marker_detection_info())

    #print('y stop')
    chassis_ctrl.stop()
    if marker[1] == 0:
        detected_Num.append(dic_insert_null)
        dic_insert_null += 1

pid_x = rm_ctrl.PIDCtrl()
pid_y = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()
variable_X = 0
variable_Y = 0
variable_Post = 0
list_MarkerList = RmList()

def vision_Select(set_time, set_distance, set_speed, set_number):
    global variable_X
    global variable_Y
    global variable_Post
    global list_MarkerList
    global pid_x
    global pid_y
    global pid_Pitch
    global pid_Yaw
    gimbal_ctrl.yaw_ctrl(0)
    gimbal_ctrl.pitch_ctrl(-20)
    vision_ctrl.set_marker_detection_distance(3)
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    pid_Yaw.set_ctrl_params(115,0,5)
    pid_Pitch.set_ctrl_params(85,0,3)
    cnt = 0
    start = time.time()
    while not cnt == 1 and (time.time() - start) <= set_time:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        #print('time :', time.time() - start)
        if list_MarkerList[1] >= 1 and set_number in list_MarkerList:    
            set_Number_Index = list_MarkerList.index(set_number)
            variable_X = list_MarkerList[set_Number_Index + 1]
            variable_Y = list_MarkerList[set_Number_Index + 2]
            pid_Yaw.set_error(variable_X - 0.5)
            pid_Pitch.set_error(0.5 - variable_Y)
            if list_MarkerList[set_Number_Index + 1] >= 0.0:
                dy = list_MarkerList[set_Number_Index + 1] - 0.5   
            else:
                dy = list_MarkerList[set_Number_Index + 1] + 0.4     
            chassis_ctrl.move_with_speed((set_distance - list_MarkerList[set_Number_Index + 4]) * set_speed, 3 * dy, pid_Yaw.get_output()) 
        else:
            chassis_ctrl.stop()
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())

def shoot(set_number):
    if sort_Dic[set_number][2] == 'point_0':
        #move_Turn(150, 90, 'left', 0.5)
        move_Turn_v5(50, -87)
        vision_Select(4, 0.25, 3, set_number)
        led_ctrl.gun_led_on()
        time.sleep(1)
        led_ctrl.gun_led_off()
        #move_Turn(150, 90, 'right', 0.5)
        move_Turn_v5(50, 2)
        robot_ctrl.set_mode(rm_define.robot_mode_free)

    if sort_Dic[set_number][2] == 'point_2':
        #move_Turn(150, 90, 'right', 0.5)
        move_Turn_v5(50, 90)
        vision_Select(4, 0.25, 3, set_number)
        led_ctrl.gun_led_on()
        time.sleep(1)
        led_ctrl.gun_led_off()
        #move_Turn(150, 90, 'left', 0.5)
        move_Turn_v5(50, 2)
        robot_ctrl.set_mode(rm_define.robot_mode_free)

    if sort_Dic[set_number][2] == 'point_13':
        vision_Select(4, 0.25, 3, set_number)
        led_ctrl.gun_led_on()
        time.sleep(1)
        led_ctrl.gun_led_off()
        robot_ctrl.set_mode(rm_define.robot_mode_free)

    if sort_Dic[set_number][2] == 'point_10':
        #move_Turn(150, 180, 'right', 0.5)
        move_Turn_v5(50, -174)
        vision_Select(4, 0.25, 3, set_number)
        led_ctrl.gun_led_on()
        time.sleep(1)
        led_ctrl.gun_led_off()
        #move_Turn(150, 180, 'right', 0.5)
        move_Turn_v5(50, 2)
        robot_ctrl.set_mode(rm_define.robot_mode_free)

def move_Turn_v2(set_speed, set_angle, set_dir, set_sleep):
    
    global init_angle
    cnt = 0
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.set_follow_chassis_offset(0)
    chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_rotate_speed(set_speed)
    if set_dir == 'right':
        chassis_ctrl.rotate(rm_define.clockwise)
    elif set_dir == 'left':
        chassis_ctrl.rotate(rm_define.anticlockwise)
    
    while not cnt == 1:
        current_Yaw = chassis_ctrl.get_attitude(rm_define.chassis_yaw)
        if (set_dir == 'right') and (current_Yaw - init_angle >= set_angle):
            chassis_ctrl.stop()
            cnt = 1
            time.sleep(set_sleep)

        elif (set_dir == 'left') and (init_angle - current_Yaw >= set_angle):
            chassis_ctrl.stop()
            cnt = 1
            time.sleep(set_sleep)

def move_Turn_v3(set_speed, set_angle, set_dir, set_sleep):
    global init_angle
    cnt = 0

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.set_follow_chassis_offset(0)
    chassis_ctrl.enable_stick_overlay()
    chassis_ctrl.set_rotate_speed(set_speed)
    if set_dir == 'right':
        chassis_ctrl.rotate(rm_define.clockwise)
    elif set_dir == 'left':
        chassis_ctrl.rotate(rm_define.anticlockwise)

    while not cnt == 1:
        current_Yaw = chassis_ctrl.get_attitude(rm_define.chassis_yaw)
        if (set_dir == 'right') and (current_Yaw - init_angle >= set_angle):
            after_Yaw = chassis_ctrl.get_attitude(rm_define.chassis_yaw)
            chassis_ctrl.stop()
            print('after_Yaw', after_Yaw)
            print('set_angle', set_angle)
            if after_Yaw > set_angle:
                chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, after_Yaw - set_angle)
                chassis_ctrl.stop()
                cnt = 1
                time.sleep(set_sleep)

        elif (set_dir == 'left') and (init_angle - current_Yaw >= set_angle):
            after_Yaw = chassis_ctrl.get_attitude(rm_define.chassis_yaw)
            chassis_ctrl.stop()
            print('after_Yaw', after_Yaw)
            print('set_angle', set_angle)
            if abs(after_Yaw) > abs(set_angle):
                chassis_ctrl.rotate_with_degree(rm_define.clockwise, abs(after_Yaw - set_angle))
                chassis_ctrl.stop()
                cnt = 1
                time.sleep(set_sleep)
                
def move_Turn_v5(set_speed, set_angle):
    cnt = 0
    init_Yaw = chassis_ctrl.get_attitude(rm_define.chassis_yaw)
    set_dir = 0
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.set_follow_chassis_offset(0)
    chassis_ctrl.enable_stick_overlay()
    

    while not cnt == 1:
        current_Yaw = chassis_ctrl.get_attitude(rm_define.chassis_yaw)
        if (-30 < abs(current_Yaw - set_angle)) and (30 > abs(current_Yaw - set_angle)):
            chassis_ctrl.set_rotate_speed(10)

        else:
            chassis_ctrl.set_rotate_speed(set_speed)

        if init_Yaw > 0:
            if set_angle >= 0:
                if 180 - init_Yaw > set_angle:
                    chassis_ctrl.rotate(rm_define.clockwise)
                    set_dir = 'right'
                else:
                    chassis_ctrl.rotate(rm_define.anticlockwise)
                    set_dir = 'left'
                if(-0.5 < abs(current_Yaw - set_angle)) and (0.5 > abs(current_Yaw - set_angle)):
                    cnt = 1
                    chassis_ctrl.stop()
                """if (set_dir == 'left') and (current_Yaw <= set_angle):
                    cnt = 1
                    chassis_ctrl.stop()
                elif (set_dir == 'right') and (current_Yaw >= abs(set_angle)):
                    cnt = 1
                    chassis_ctrl.stop()"""
            if set_angle < 0:
                if init_Yaw - 180 <= set_angle:
                    chassis_ctrl.rotate(rm_define.anticlockwise)
                    set_dir = 'left'
                else:
                    chassis_ctrl.rotate(rm_define.clockwise)
                    set_dir = 'right'
                if(-0.5 < abs(current_Yaw - set_angle)) and (0.5 > abs(current_Yaw - set_angle)):
                    cnt = 1
                    chassis_ctrl.stop()
                """if (set_dir == 'left') and (current_Yaw <= set_angle):
                    cnt = 1
                    chassis_ctrl.stop()
                elif (set_dir == 'right') and (abs(current_Yaw) <= abs(set_angle)):
                    cnt = 1
                    chassis_ctrl.stop()"""
        if init_Yaw < 0:
            if set_angle >= 0:
                if 180 + init_Yaw > set_angle:
                    chassis_ctrl.rotate(rm_define.clockwise)
                    set_dir = 'right'
                else:
                    chassis_ctrl.rotate(rm_define.anticlockwise)
                    set_dir = 'left'
                if(-0.5 < abs(current_Yaw - set_angle)) and (0.5 > abs(current_Yaw - set_angle)):
                    cnt = 1
                    chassis_ctrl.stop()
                """if (set_dir == 'left') and (abs(current_Yaw) <= set_angle):
                    cnt = 1
                    chassis_ctrl.stop()
                elif (set_dir == 'right') and (current_Yaw >= set_angle):
                    cnt = 1
                    chassis_ctrl.stop()"""
            if set_angle < 0:
                if init_Yaw + 180 < set_angle:
                    chassis_ctrl.rotate(rm_define.anticlockwise)
                    set_dir = 'left'
                else:
                    chassis_ctrl.rotate(rm_define.clockwise)
                    set_dir = 'right'
                if(-0.5 < abs(current_Yaw - set_angle)) and (0.5 > abs(current_Yaw - set_angle)):
                    cnt = 1
                    chassis_ctrl.stop()
                """if (set_dir == 'left') and (abs(current_Yaw) >= abs(set_angle)):
                    cnt = 1
                    chassis_ctrl.stop()
                elif (set_dir == 'right') and (abs(current_Yaw) <= abs(set_angle)):
                    cnt = 1
                    chassis_ctrl.stop()"""

    time.sleep(0.5)
def start():

    init()
    sum_List.append(line_Tracking_With_Marker(0.5, 'blue', 1, 10))
    sum_List.append(line_Tracking_With_Marker(0.5, 'blue', 1, 7.5))
    print(sum_List)
    for i in range(len(sum_List[0])):
        if sum_List[0][i] == sum_List[1][i]:
            list_ShootList.append(sum_List[0][i])
    list_ShootList.reverse()
    user_defined_Shoot()

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow) 

    move_Axis(0.3, -60, 1.3, 0.5)
    move_Axis(0.3, 0, 0.2, 0.5)
    #move_Turn(100, 180, 'left', 0.5)
    move_Turn_gimbal(100, 183, 0.5)

    move_Axis_Stop_Marker(0.3, 47, 0.5)
    move_Axis(0.3, 180, 0.2, 0.5)
    vision_Select(5, 0.48, 1, 47)