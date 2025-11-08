import requests
from time import time, sleep
from geometry_msgs.msg import Twist

class MinecraftOverrideConfig:
    def __init__(self, override: bool = False):
        self.minecraft_override = override
        self.minecraft_server_url = "http://lablab.local:25565"  # Example URL
        self.last_output = Twist()

    def init_world(self):
        # send get request to minecraft server /init_world endpoint
        try:
            response = requests.get(f"{self.minecraft_server_url}/init_world")
            if response.status_code == 200:
                print("Successfully initialized Minecraft world.")
            else:
                print(f"Failed to initialize Minecraft world. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error initializing Minecraft world: {e}")

    def setpoint(self, angle: float):
        # send request to minecraft server /setpoint endpoint
        try:
            data = {"setpoint": angle}
            response = requests.post(f"{self.minecraft_server_url}/setpoint", json=data)
            if response.status_code == 200:
                print("Successfully sent Setpoint message to Minecraft server.")
            else:
                print(f"Failed to send Setpoint message. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending Setpoint message to Minecraft server: {e}")

    def switch_camera(self, front=True):
        # send get request to minecraft server /switch_camera endpoint
        try:
            response = requests.get(f"{self.minecraft_server_url}/{"front" if front else "bottom"}_camera")
            if response.status_code == 200:
                print("Successfully switched camera on Minecraft server.")
            else:
                print(f"Failed to switch camera. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error switching camera on Minecraft server: {e}")

    def send_twist_message(self, twist_msg : Twist):
        # send request to minecraft server /twist endpoint
        if self.last_output == twist_msg:
            return  # No change in command, skip sending
        try:
            self.last_output = twist_msg
            data = {
                "linear": {
                    "x": twist_msg.linear.x,
                    "y": twist_msg.linear.y,
                    "z": twist_msg.linear.z
                },
                "angular": {
                    "x": twist_msg.angular.x,
                    "y": twist_msg.angular.y,
                    "z": twist_msg.angular.z
                }
            }
            response = requests.post(f"{self.minecraft_server_url}/twist", json=data)
            
            if response.status_code == 200:
                print("Successfully sent Twist message to Minecraft server.")
            else:
                print(f"Failed to send Twist message. Status code: {response.status_code}")
            
            # if angular z > 0, instead of sending twist, send to /setpoint endpoint with -90 or 90
            if abs(twist_msg.angular.z) > 0.1:
                angle = 90 if twist_msg.angular.z > 0 else -90
                self.setpoint(angle)
                
        except Exception as e:
            print(f"Error sending Twist message to Minecraft server: {e}")


# Workshop part 1 - Script-based automation
if __name__ == "__main__":
    sleep(2)  # wait for minecraft server to start
    moc = MinecraftOverrideConfig(override=True)
    
    def send_command(linear_x=0.0, linear_y=0.0, angular_z=0.0, name=""):
        test_twist = Twist()
        test_twist.linear.x = linear_x
        test_twist.linear.y = linear_y
        test_twist.angular.z = angular_z
        if name:
            print(f"Sending {name} command")
        moc.send_twist_message(test_twist)
    
    def execute_sequence(actions):
        for action, duration in actions:
            action()
            sleep(duration)

    while True:
        execute_sequence([
            (moc.init_world, 2),
            (lambda: moc.switch_camera(front=False), 1),
            (lambda: moc.switch_camera(front=True), 1),
            (lambda: send_command(linear_x=1.0, name="forward"), 10),
            (lambda: send_command(name="stop"), 1),
            (lambda: send_command(linear_y=1.0, name="left"), 6),
            (lambda: send_command(name="stop"), 1),
            (lambda: send_command(linear_x=1.0, name="forward"), 20),
            (lambda: send_command(name="stop"), 1),
            (lambda: moc.switch_camera(front=False), 1),
            (lambda: send_command(linear_x=1.0, name="forward"), 1),
            (lambda: send_command(name="stop"), 1),
            (lambda: moc.switch_camera(front=True), 1),
            (lambda: send_command(name="stop"), 1),
            (lambda: send_command(linear_x=-1.0, name="backward"), 5),
            (lambda: send_command(name="stop"), 1),
            (lambda: moc.setpoint(-90), 1),
            (lambda: send_command(linear_x=1.0, linear_y=-1.0, name="right+forward"), 6),
            (lambda: send_command(name="stop"), 1),
        ])
