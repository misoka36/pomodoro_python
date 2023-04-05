# Pomodoro Timer
# 通知はWindowsのみ対応

import time
import os
import platform
import ctypes

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def notify(title, message):
    if platform.system() == "Windows":
        ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)

def countdown(duration, label):
    seconds = duration * 60
    while seconds > 0:
        clear_console()
        print(f"{label}: {seconds // 60:02d}:{seconds % 60:02d}")
        time.sleep(1)
        seconds -= 1

def pomodoro_timer(work_duration=25, break_duration=5, num_sessions=4):
    session_count = 0

    while session_count < num_sessions:
        countdown(work_duration, f"Session {session_count + 1} - Work")
        notify("Pomodoro Timer", f"Session {session_count + 1} finished. Time for a break!")
        session_count += 1

        if session_count < num_sessions:
            countdown(break_duration, f"Session {session_count} - Break")
            notify("Pomodoro Timer", f"Break is over. Time to start session {session_count + 1}!")
        else:
            print("All sessions completed. Good job!")
            notify("Pomodoro Timer", "All sessions completed. Good job!")

if __name__ == "__main__":
    pomodoro_timer(1, 1)

