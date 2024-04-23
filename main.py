import pyagxrobots
import time

scoutMini = pyagxrobots.pysdkugv.ScoutMiniBase()
scoutMini.EnableCAN()


def sample_motion():
    num = 5
    while num > 0:
        scoutMini.SetMotionCommand(linear_vel=0.1)
        print(scoutMini.GetLinearVelocity())
        time.sleep(0.3)
        num -= 1


if __name__ == '__main__':
    sample_motion()
