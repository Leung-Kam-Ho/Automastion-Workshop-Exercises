# Automation Workshop

This repository serves as an educational resource for learning different approaches to automation, using Minecraft as a practical example. The Minecraft world simulates the SAUVC competition pool setup, providing a safe and accessible environment for testing automation algorithms. The Answer to this workshop can be found [here](https://github.com/Leung-Kam-Ho/Automation-Workshop) with limited access. The workshop covers three progressive levels of automation complexity:

## Workshop Levels

### 1. Script-Based Automation

Learn the fundamentals of automation through direct scripting. This approach involves writing sequential commands to control game actions.

**Key Files:**
- `Script_Based_Auto.py` - Demonstrates basic script-based automation with movement sequences
- `Minecraft_Tool/minecraft_override_config.py` - Client library for sending commands to Minecraft

**Challenges:**
- Implement additional movement patterns
- The arena environment is fixed
- Use script based logic to walk through the Gate and reach the target area in a specific path

### 2. Behaviour Tree Based Automation
Advance to more sophisticated automation using behaviour trees. This approach provides better structure and modularity for complex decision-making processes.

https://github.com/user-attachments/assets/a52e6e98-5778-4f9f-8694-226901665de7

**Key Files:**
- `BehaviourTree_Based_Auto.py` - Demonstrates behaviour tree-based automation
  
**Challenges:**
- Implement additional action nodes and composite nodes
- The arena environment is fixed
- Use Behaviour Tree based logic to walk through the Gate and reach the target area in a specific path

**Dependencies:**
- `py-trees` - For behaviour tree logic


### 3. YOLO + Behaviour Tree Automation
Combine computer vision with behaviour trees for intelligent automation. Use YOLO (You Only Look Once) object detection to perceive the game environment and make decisions accordingly.

https://github.com/user-attachments/assets/08648b6e-d58c-47cc-821f-c0e940ea29cf

**Key Files:**
- `YOLO_BehaviourTree_Based_Auto.py` - Demonstrates YOLO + behaviour tree automation

**Challenges:**
- Integrate YOLO object detection into the behaviour tree
- Implement additional action nodes and composite nodes
- The arena environment may vary, requiring dynamic decision-making
- Use YOLO + Behaviour Tree based logic to walk through the Gate, go to the blue pail (bucket), and hit all 3 colored poles in the target area

**Dependencies:**
- `ultralytics` - YOLO implementation for object detection
- `py-trees` - For behaviour tree logic

## Setup

### Prerequisites
- Python 3.12+
- Minecraft Java Edition
- UV package manager (recommended)
- ROS 2

### Installation
```bash
# Clone the repository
git clone https://github.com/Leung-Kam-Ho/Automation-Workshop.git
cd automation-workshop

# Install dependencies
uv sync
```

### Minecraft Server Setup
The project communicates with a local Minecraft server running on port 25565. The server simulates ROS-like control by translating commands into keyboard inputs for Minecraft. Download the CurseForge modpack [here]() and load it into your Minecraft server.

**To run the Minecraft command server:**
```bash
uv run python Minecraft_Tool/minecraft_command_server.py
```

![Minecraft Virtual Environment](Media/Minecraft_Screenshoot.png)

## Project Structure
```
├── Minecraft_Tool/
│   ├── minecraft_command_server.py    # Flask server for Minecraft control
│   └── minecraft_override_config.py    # Client library for server communication
├── Script_Based_Auto.py                # Level 1: Script-based automation example
├── BehaviourTree_Based_Auto.py         # Level 2: Behaviour tree-based automation example
├── YOLO_BehaviourTree_Based_Auto.py    # Level 3: YOLO + behaviour tree-based automation example
├── main.py                            # Project entry point
├── pyproject.toml                     # Project configuration
└── README.md                          # This file
```

## Getting Started

1. **Start the Minecraft Command Server:**
   ```bash
   uv run python Minecraft_Tool/minecraft_command_server.py
   ```

2. **Run Script-Based Automation:**
   ```bash
   uv run python Script_Based_Auto.py
   ```

3. **Explore Behaviour Trees:**
   Implement your own behaviour tree logic using the `py-trees` library.

4. **Add Computer Vision:**
   Integrate YOLO for object detection and combine with behaviour trees for advanced automation.

## Learning Objectives

By completing this workshop, you'll learn:
- Basic scripting for automation tasks
- Behaviour tree design patterns
- Computer vision integration with YOLO
- ROS-like message passing concepts
- Modular automation architecture

## Contributing

This is an educational repository. Feel free to enhance the examples or add new automation levels while maintaining the progressive learning structure.
