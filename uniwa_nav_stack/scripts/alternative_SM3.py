#!/usr/bin/env python

import rospy
from fix_arena import Fix
from std_msgs.msg import String
import smach
import time
from smach_ros import SimpleActionState, IntrospectionServer
from smach import State, StateMachine
from PHASE_1 import ShutDown, Move, CountPeople, TrackItems, AnnouncePhaseOne, GetStatus
from PHASE_2 import GetServingTables, GetSpeechOrder
from PHASE_3 import Wait, SpawnOrder, ConfirmOrder, CorrectOrder, Pickuporder, Serve
from head import move_head_centre, move_head_up, move_head_down, move_head_left, move_head_right
from coordinates import Coordinates
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


# main with state machines
def main():
    c = Coordinates()
    c.init_location()
    #c.init_location_close()

    home = c.home
    paso = c.paso
    resting_area = c.resting_area
    table1 = c.table1
    table2 = c.table2
    table3 = c.table3
    table4 = c.table4
    table5 = c.table5
    table6 = c.table6
    rospy.init_node('smach_example_state_machine')
    pubPhrase = rospy.Publisher('waitbot/tts/phrase', String, queue_size=5)
    print ("init")



#=================================================================
##PHASE1##
#=================================================================

    phase1 = smach.StateMachine(outcomes=['finished'])

    with phase1:

        smach.StateMachine.add('UPVIEW0',
                               move_head_up('Moving head up'),
                               transitions={'done':'WAIT0'})
        smach.StateMachine.add('WAIT0',
                               Wait('resting'),
                                transitions={'done':'TABLE1'})

        # -------------------------- 1 -----------------------------

        smach.StateMachine.add('TABLE1',
                               Move(table1, 'table1'),
                               transitions={'done':'WAIT1'})
        smach.StateMachine.add('WAIT1',
                               Wait('resting'),
                                transitions={'done':'PEOPLE1'})
        smach.StateMachine.add('PEOPLE1',
                               CountPeople('Counting People'),
                               transitions={'done':'DOWNVIEW1'})
        smach.StateMachine.add('DOWNVIEW1',
                               move_head_down('Moving head down'),
                               transitions={'done':'WAIT11'})
        smach.StateMachine.add('WAIT11',
                               Wait('Please give'),
                                transitions={'done':'ITEMS1'})
        smach.StateMachine.add('ITEMS1',
                               TrackItems('Tracking Items'),
                               transitions={'done':'STATUS1'})
        smach.StateMachine.add('STATUS1',
                               GetStatus('table1', 'Getting table status'),
                               transitions={'done':'UPVIEW1'})

        # -------------------------- 2 -----------------------------
        smach.StateMachine.add('UPVIEW1',
                               move_head_up('Moving head up'),
                               transitions={'done':'TABLE2'})
        smach.StateMachine.add('TABLE2',
                               Move(table2, 'table2'),
                               transitions={'done':'WAIT2'})
        smach.StateMachine.add('WAIT2',
                               Wait('resting'),
                                transitions={'done':'PEOPLE2'})
        smach.StateMachine.add('PEOPLE2',
                               CountPeople('Counting People'),
                               transitions={'done':'DOWNVIEW2'})
        smach.StateMachine.add('DOWNVIEW2',
                               move_head_down('Moving head down'),
                               transitions={'done':'WAIT22'})
        smach.StateMachine.add('WAIT22',
                               Wait('Please give'),
                                transitions={'done':'ITEMS2'})
        smach.StateMachine.add('ITEMS2',
                               TrackItems('Tracking Items'),
                               transitions={'done':'STATUS2'})
        smach.StateMachine.add('STATUS2',
                               GetStatus('table2', 'Getting table status'),
                               transitions={'done':'UPVIEW2'})

        # -------------------------- 3 -----------------------------
        smach.StateMachine.add('UPVIEW2',
                               move_head_up('Moving head up'),
                               transitions={'done':'TABLE3'})
        smach.StateMachine.add('TABLE3',
                               Move(table3, 'table3'),
                               transitions={'done':'WAIT3'})
        smach.StateMachine.add('WAIT3',
                               Wait('resting'),
                                transitions={'done':'PEOPLE3'})
        smach.StateMachine.add('PEOPLE3',
                               CountPeople('Counting People'),
                               transitions={'done':'DOWNVIEW3'})
        smach.StateMachine.add('DOWNVIEW3',
                               move_head_down('Moving head down'),
                               transitions={'done':'WAIT33'})
        smach.StateMachine.add('WAIT33',
                               Wait('Please give'),
                                transitions={'done':'ITEMS3'})
        smach.StateMachine.add('ITEMS3',
                               TrackItems('Tracking Items'),
                               transitions={'done':'STATUS3'})
        smach.StateMachine.add('STATUS3',
                               GetStatus('table3', 'Getting table status'),
                               transitions={'done':'UPVIEW4'})

        # -------------------------- 4 -----------------------------
        smach.StateMachine.add('UPVIEW4',
                               move_head_up('Moving head up'),
                               transitions={'done':'TABLE4'})
        smach.StateMachine.add('TABLE4',
                               Move(table4, 'table4'),
                               transitions={'done':'WAIT4'})
        smach.StateMachine.add('WAIT4',
                               Wait('resting'),
                                transitions={'done':'PEOPLE4'})
        smach.StateMachine.add('PEOPLE4',
                               CountPeople('Counting People'),
                               transitions={'done':'DOWNVIEW4'})
        smach.StateMachine.add('DOWNVIEW4',
                               move_head_down('Moving head down'),
                               transitions={'done':'WAIT44'})
        smach.StateMachine.add('WAIT44',
                               Wait('Please give'),
                                transitions={'done':'ITEMS4'})
        smach.StateMachine.add('ITEMS4',
                               TrackItems('Tracking Items'),
                               transitions={'done':'STATUS4'})
        smach.StateMachine.add('STATUS4',
                               GetStatus('table4', 'Getting table status'),
                               transitions={'done':'UPVIEW5'})

        # -------------------------- 5 -----------------------------
        smach.StateMachine.add('UPVIEW5',
                               move_head_up('Moving head up'),
                               transitions={'done':'TABLE5'})
        smach.StateMachine.add('TABLE5',
                               Move(table5, 'table5'),
                               transitions={'done':'WAIT5'})
        smach.StateMachine.add('WAIT5',
                               Wait('resting'),
                                transitions={'done':'PEOPLE5'})
        smach.StateMachine.add('PEOPLE5',
                               CountPeople('Counting People'),
                               transitions={'done':'DOWNVIEW5'})
        smach.StateMachine.add('DOWNVIEW5',
                               move_head_down('Moving head down'),
                               transitions={'done':'WAIT55'})
        smach.StateMachine.add('WAIT55',
                               Wait('Please give'),
                                transitions={'done':'ITEMS5'})
        smach.StateMachine.add('ITEMS5',
                               TrackItems('Tracking Items'),
                               transitions={'done':'STATUS5'})
        smach.StateMachine.add('STATUS5',
                               GetStatus('table5', 'Getting table status'),
                               transitions={'done':'UPVIEW6'})

        # -------------------------- 6 -----------------------------
        smach.StateMachine.add('UPVIEW6',
                               move_head_up('Moving head up'),
                               transitions={'done':'TABLE6'})
        smach.StateMachine.add('TABLE6',
                               Move(table6, 'table6'),
                               transitions={'done':'WAIT6'})
        smach.StateMachine.add('WAIT6',
                               Wait('resting'),
                                transitions={'done':'PEOPLE6'})
        smach.StateMachine.add('PEOPLE6',
                               CountPeople('Counting People'),
                               transitions={'done':'DOWNVIEW6'})
        smach.StateMachine.add('DOWNVIEW6',
                               move_head_down('Moving head down'),
                               transitions={'done':'WAIT66'})
        smach.StateMachine.add('WAIT66',
                               Wait('Please give'),
                                transitions={'done':'ITEMS6'})
        smach.StateMachine.add('ITEMS6',
                               TrackItems('Tracking Items'),
                               transitions={'done':'STATUS6'})
        smach.StateMachine.add('STATUS6',
                               GetStatus('table6', 'Getting table status'),
                               transitions={'done':'RESTINGAREA'})


        smach.StateMachine.add('RESTINGAREA',
                               Move(resting_area, 'resting area'),
                               transitions={'done':'VIEW'})
        smach.StateMachine.add('VIEW',
                               move_head_centre('Moving head up'),
                               transitions={'done':'finished'})

    outcome = phase1.execute()

#=================================================================
##PHASE2##
#=================================================================

#     pubPhrase.publish('Initiating Phase 2')
#
#     phase2 = smach.StateMachine(outcomes=['finished'])
#
#     with phase2:
#         smach.StateMachine.add('GETSERVING',
#                                 GetServingTables('get serving'),
#                                 transitions={'done':'SPEECH'})
#         smach.StateMachine.add('SPEECH',
#                                 GetSpeechOrder('INITIATE SPEECH'),
#                                 transitions={'done':'finished'})
#         # smach.StateMachine.add('TAKEORDER',
#         #                         Serve('Serving....'),
#         #                         transitions={'done':'TABLE1'})
#
#
#     outcome2 = phase2.execute()
#
# #=================================================================
# ##PHASE3##
# #=================================================================
#
#     pubPhrase.publish('Initiating Phase 2')
#
#
#     phase3 = smach.StateMachine(outcomes=['finished'])
#
#
#     with phase3:
#
#
#         smach.StateMachine.add('PASO',
#                                 Move(paso),
#                                 transitions={'done':'SPAWNORDER'})
#         smach.StateMachine.add('SPAWNORDER',
#                                 SpawnOrder('Spawning order...'),
#                                 transitions={'done':'WAIT'})
#         smach.StateMachine.add('WAIT',
#                                 Wait('Please give the correct order'),
#                                 transitions={'skip':'finished', 'done':'finished'})
    #     smach.StateMachine.add('CONFIRMORDER',
    #                             ConfirmOrder('Confirming'),
    #                             transitions={'correct':'PICKUP', 'false':'CORRECTORDER'})
    #     smach.StateMachine.add('CORRECTORDER',
    #                             CorrectOrder('Correcting the order'),
    #                             transitions={'done':'WRONGORDER'})
    #     smach.StateMachine.add('WRONGORDER',
    #                             Wait('Please give the correct order'),
    #                             transitions={'skip':'CONFIRMORDER', 'done':'CONFIRMORDER'})
    #     smach.StateMachine.add('PICKUP',
    #                            Pickuporder('Picking items'),
    #                            transitions={'done':'TABLE2'})
    #     smach.StateMachine.add('TABLE2',
    #                             Move(table2),
    #                             transitions={'done':'SERVE'})
    #     smach.StateMachine.add('SERVE',
    #                            Serve('Serving'),
    #                            transitions={'done':'finished'})
    #
    #outcome3 = phase3.execute()


    #rospy.spin()


if __name__ == '__main__':
  try:
    main()
  except rospy.ROSInterruptException:
    rospy.loginfo("Test is complete")
