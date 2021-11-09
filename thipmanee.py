#!/usr/bin/env python #เป็นการทำให้ scripts ทั้งหมดทำงานเป็น python scripts

import rospy #เราต้อง import rospy ถ้าต้องการเขียน ROS node
from std_msgs.msg import String #std_msgs.msg ทำให้เรา publishing ข้อความ string ได้

def talker():
    pub = rospy.Publisher('Thipmaneetopic', String, queue_size=10) #เป็นการประกาศว่า node กำลัง publishing ข้อความไปยัง Thipmanee_topic โดยใช้ข้อความชนิด string
    rospy.init_node('Thipmanee', anonymous=True) #เป็นการบอก rospy ว่า node ของเราชื่ออะไรจนกว่า rospy จะได้รับข้อมูล
    rate = rospy.Rate(5) # 5hz #เป็นการ looping คำสั่งที่เราต้องการได้ตามความต้องการของเรา 
    while not rospy.is_shutdown(): #เราจะใช้คำสั่งนี้ก็ต่อเมื่อ ต้องการจะ publish topic ด้วยความเร็วปัจุบันคือ 5 hz
        name_str = "My name is Thipmanee %s" % rospy.get_time() #แสดงข้อความที่เราใส่เข้าไปและแสดงเวลาปัจจุบัน
        rospy.loginfo(name_str) #คำสั่งนี้ทำหน้าที่3อย่างคือ จะปริ้นท์ข้อความบนหน้าจอ และจะถูกเขียนลงใน Node log file และ rosout
        pub.publish(name_str) #การทำงานของ pub.publish คือการ publishes ข้อความ string ไปยัง Thipmanee_topic ของเรา
        rate.sleep() #ทำหน้าที่ในการ sleep loop ของเราให้นานเท่าที่เราตั้งค่า rate เอาไว้

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
