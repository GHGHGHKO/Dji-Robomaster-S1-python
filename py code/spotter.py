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
            variable_StartFlag = 1 #종료

def start():
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
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.set_rotate_speed(180)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,90)
    user_defined_Save()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    user_defined_Shoot()
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    led_ctrl.gun_led_on()
