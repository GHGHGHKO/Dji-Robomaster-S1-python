global marker
marker = RmList()
global sight
sight = RmList()

def start():
    global marker
    init()
    chassis_ctrl.set_trans_speed(0.5)
    chassis_ctrl.move_with_distance(45,0.7)
    time.sleep(0.5)
    
    xs = chassis_ctrl.get_position_based_power_on(rm_define.chassis_forward)
    ys = chassis_ctrl.get_position_based_power_on(rm_define.chassis_translation)
    position_y(-90,0,0.3)
    xk = chassis_ctrl.get_position_based_power_on(rm_define.chassis_forward)
    fire()
    chassis_ctrl.set_trans_speed(0.5)
    chassis_ctrl.move_with_distance(180,xk-xs+0.05)
    position_y(-180,90,0.3)
    yk = chassis_ctrl.get_position_based_power_on(rm_define.chassis_translation)
    fire()
    chassis_ctrl.set_trans_speed(0.5)
    chassis_ctrl.move_with_distance(0,xk-ys)
    xk = chassis_ctrl.get_position_based_power_on(rm_define.chassis_forward)
    yk = chassis_ctrl.get_position_based_power_on(rm_define.chassis_translation)
    position_x(0,0,0.3,0.22)
    xt = chassis_ctrl.get_position_based_power_on(rm_define.chassis_forward)
    fire()
    chassis_ctrl.set_trans_speed(0.5)
    chassis_ctrl.move_with_distance(180,xt-xk)
    position_x(90,90,0.3,0.22)
    yt = chassis_ctrl.get_position_based_power_on(rm_define.chassis_translation)
    fire()
    chassis_ctrl.set_trans_speed(0.5)
    chassis_ctrl.move_with_distance(-90,0.15)
    chassis_ctrl.move_with_distance(0,xt-xk)
    chassis_ctrl.move_with_distance(45,0.7)
    media_ctrl.play_sound(rm_define.media_sound_recognize_success)
   
def init():
    global sight
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(270)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(0.5)
    gun_ctrl.set_fire_count(1)
    sight = RmList(media_ctrl.get_sight_bead_position())
    gimbal_ctrl.pitch_ctrl(-15)

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

def position_y(gimbal_yaw,direction,speed):
    global marker
    gimbal_ctrl.yaw_ctrl(gimbal_yaw)
    marker = RmList(vision_ctrl.get_marker_detection_info())
    chassis_ctrl.move_degree_with_speed(speed,direction)
    while marker[1] < 1:
        marker = RmList(vision_ctrl.get_marker_detection_info())
    while abs(marker[3]-0.5) > 0.05:
        chassis_ctrl.move_degree_with_speed(0.1,direction)
        marker = RmList(vision_ctrl.get_marker_detection_info())
        while marker[1] < 1:
            marker = RmList(vision_ctrl.get_marker_detection_info())
    chassis_ctrl.stop()

def fire():
    global sight
    global marker
    x0 = gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_yaw)
    y0 = gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_pitch)
    x = 96 * ( marker[3] - sight[1] ) + x0
    y = 54 * ( sight[2] - marker[4] ) + y0
    gimbal_ctrl.angle_ctrl(x,y)
    led_ctrl.gun_led_on()
    gun_ctrl.fire_once()
    time.sleep(1)
    led_ctrl.gun_led_off()
    gimbal_ctrl.angle_ctrl(x0,y0)