import turtle, winsound
from time import sleep, perf_counter

SOUND_FILE: str = "./Alarm.wav"
FONT: tuple[str, int, str] = ("Arial", 90, "bold")

pen = turtle.Turtle()
pen.hideturtle()
def setup_window(mins: int, secs: int):
    timer: str = f"{mins:02d} : {secs:02d}"
    screen = turtle.Screen()
    screen.title(f"Countdown Timer ({timer})")
    screen.clear()
    screen.bgcolor("yellow")

    def update_time():
        pen.write(timer, align="center", font=FONT)
        if not mins and not secs:
            pen.sety(pen.ycor() - FONT[1] / 2 - 30)

            # Flash text
            pen.write("Time's up!", align="center", font=(FONT[0], FONT[1] - 20, FONT[2]))

    update_time()

def countdown(sec_input: int):
    """start_perf and end_perf used for accurate countdown as it accounts for the time to setup"""

    while True:
        if sec_input >= 0:
            start_perf: float = perf_counter()

            mins, secs = divmod(sec_input, 60)
            setup_window(mins, secs)
            if sec_input <= 0:
                break

            end_perf: float = perf_counter()

            sleep(1 - (start_perf - end_perf))
            sec_input -= 1
    # TImer completed
    winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME)
    print("Time's up!")


time = int(input("Enter start time in seconds: "))
countdown(time)