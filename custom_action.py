from time import time
from geometry_msgs.msg import Twist  # if you are not using ROS, you can comment this line out and create a mock Twist class
import py_trees
from Minecraft_Tool.minecraft_override_config import MinecraftOverrideConfig
from YOLO_Tool.get_detect_info import get_detection_info


class InitWorld(py_trees.behaviour.Behaviour):
    def __init__(self, moc : MinecraftOverrideConfig):
        super().__init__("InitWorld")
        self.moc = moc
        self._done = False

    def initialise(self):
        self.moc.init_world()
        self._done = False
        self._start_time = time()

    def update(self):
        if not self._done:
            if time() - self._start_time >= 2:
                self._done = True
                return py_trees.common.Status.SUCCESS
            else:
                return py_trees.common.Status.RUNNING
        return py_trees.common.Status.SUCCESS


class SwitchCameraFront(py_trees.behaviour.Behaviour):
    def __init__(self, moc : MinecraftOverrideConfig):
        super().__init__("SwitchCameraFront")
        self.moc = moc
        self._done = False

    def initialise(self):
        self.moc.switch_camera(front=True)
        self._done = False
        self._start_time = time()

    def update(self):
        if not self._done:
            if time() - self._start_time >= 1:
                self._done = True
                return py_trees.common.Status.SUCCESS
            else:
                return py_trees.common.Status.RUNNING
        return py_trees.common.Status.SUCCESS


class SwitchCameraBottom(py_trees.behaviour.Behaviour):
    def __init__(self, moc : MinecraftOverrideConfig):
        super().__init__("SwitchCameraBottom")
        self.moc = moc
        self._done = False

    def initialise(self):
        self.moc.switch_camera(front=False)
        self._done = False
        self._start_time = time()

    def update(self):
        if not self._done:
            if time() - self._start_time >= 1:
                self._done = True
                return py_trees.common.Status.SUCCESS
            else:
                return py_trees.common.Status.RUNNING
        return py_trees.common.Status.SUCCESS



class Move(py_trees.behaviour.Behaviour):
    def __init__(self, node : MinecraftOverrideConfig, twist : Twist):
        super().__init__("Move")
        self.node = node
        self.twist = twist

    def initialise(self):
        self.node.send_twist_message(self.twist)

    def update(self):
        return py_trees.common.Status.SUCCESS



class MoveForward(py_trees.behaviour.Behaviour):
    def __init__(self, node : MinecraftOverrideConfig, duration):
        super().__init__("MoveForward")
        self.node = node
        self.duration = duration

    def initialise(self):
        twist = Twist()
        twist.linear.x = 1.0
        self._move = Move(self.node, twist)
        self._move.initialise()
        self._start_time = time()

    def update(self):
        elapsed = time() - self._start_time
        remaining = max(0, self.duration - elapsed)
        self.feedback_message = f"Moving forward... Time left: {remaining:.1f}s"
        return py_trees.common.Status.SUCCESS if elapsed >= self.duration else py_trees.common.Status.RUNNING

    def terminate(self, new_status):
        twist = Twist()
        stop = Move(self.node, twist)
        stop.initialise()


class Stop(py_trees.behaviour.Behaviour):
    def __init__(self, node : MinecraftOverrideConfig, duration):
        super().__init__("Stop")
        self.node = node
        self.duration = duration

    def initialise(self):
        twist = Twist()
        self._move = Move(self.node, twist)
        self._move.initialise()
        self._start_time = time()

    def update(self):
        elapsed = time() - self._start_time
        remaining = max(0, self.duration - elapsed)
        self.feedback_message = f"Stopping... Time left: {remaining:.1f}s"
        return py_trees.common.Status.SUCCESS if elapsed >= self.duration else py_trees.common.Status.RUNNING


# 1. Create a MoveRight behaviour


# 2. Create a MoveLeft behaviour


# 3. Create a MoveBackward behaviour

class Yaw(py_trees.behaviour.Behaviour):
    def __init__(self, node : MinecraftOverrideConfig, yaw : float):
        super().__init__("Yaw")
        self.node = node
        self.yaw = yaw
        self._done = False

    def initialise(self):
        self.node.setpoint(self.yaw)
        self._done = False
        self._start_time = time()

    def update(self):
        if not self._done:
            if time() - self._start_time >= 1:
                self._done = True
                return py_trees.common.Status.SUCCESS
            else:
                return py_trees.common.Status.RUNNING
        return py_trees.common.Status.SUCCESS

# YOLO Detection Related Behaviours

class DetecedObject(py_trees.behaviour.Behaviour):
    def __init__(self, target_class: str, conf_threshold: float = 0.5):
        super().__init__("DetectedObject")
        self.target_class = target_class
        self.conf_threshold = conf_threshold

    def update(self):
        detection_info = get_detection_info()
        if detection_info:
            classes = detection_info.get("classes", [])
            scores = detection_info.get("confidences", [])

            for cls, score in zip(classes, scores):
                if cls == self.target_class and score >= self.conf_threshold:
                    self.feedback_message = f"Detected {cls} with confidence {score:.2f}"
                    return py_trees.common.Status.SUCCESS

        self.feedback_message = f"{self.target_class} not detected or confidence too low."
        return py_trees.common.Status.FAILURE

# 4. Create a MoveBasedOnDetection behaviour