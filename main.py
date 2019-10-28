import time
from pymouse import *
from pykeyboard import *
import random

START_DELAY = 5  # second
WORLD_MSG_SHORTCUT = '1'
TRADE_MSG_SHORTCUT = '2'


class AutoSendMsg:
    mouse = PyMouse()
    keyboard = PyKeyboard()
    rolePosition = 0

    def __init__(self, world_msg_shortcut='1', trade_msg_shortcut='2'):
        self.world_msg_shortcut = world_msg_shortcut
        self.trade_msg_shortcut = trade_msg_shortcut

    def send_world_msg(self):
        self.keyboard.press_key(self.world_msg_shortcut)
        self.keyboard.release_key(self.world_msg_shortcut)

    def send_trade_msg(self):
        self.keyboard.press_key(self.trade_msg_shortcut)
        self.keyboard.release_key(self.trade_msg_shortcut)

    def move_left(self):
        self.keyboard.press_key('a')
        time.sleep(1)
        self.keyboard.release_key('a')
        self.rolePosition -= 1

    def move_right(self):
        self.keyboard.press_key('d')
        time.sleep(1)
        self.keyboard.release_key('d')
        self.rolePosition += 1

    def jump(self):
        self.keyboard.press_key(self.keyboard.space_key)
        self.keyboard.release_key(self.keyboard.space_key)

    def move_role(self):
        move_type = random.randint(0, 2)
        if move_type == 0:  # left
            if self.rolePosition > -5:
                self.move_left()
            else:
                self.move_right()
        elif move_type == 1:    # right
            if self.rolePosition < 5:
                self.move_right()
            else:
                self.move_left()
        elif move_type == 2:    # jump
            self.jump()


def main():
    time.sleep(START_DELAY)
    auto_send_msg = AutoSendMsg(WORLD_MSG_SHORTCUT, TRADE_MSG_SHORTCUT)
    world_msg_times = 0
    while True:
        # role move
        auto_send_msg.move_role()
        time.sleep(2)

        # send msg
        if world_msg_times >= 5:
            auto_send_msg.send_trade_msg()
            world_msg_times = 0
        else:
            auto_send_msg.send_world_msg()
            world_msg_times += 1
        time.sleep(random.randint(23, 28))


if __name__ == '__main__':
    main()

