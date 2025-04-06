import subprocess

print("Training the model...")
subprocess.run(["python", "training.py"])

print("GUI is starting...")
subprocess.run(["python", "GUI.py"])