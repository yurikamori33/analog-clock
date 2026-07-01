import math
import datetime
import PySimpleGUI as sg

CENTER_X = 200
CENTER_Y = 200

def main():
    layout = [
        [sg.Canvas(
            key='-canvas-',
            size=(CENTER_X*2, CENTER_Y*2),
            background_color='white'
            )],
        [sg.Button('終了')]]

    window = sg.Window('アナログ時計', layout)
    canvas = window['-canvas-']

    while True:
        event, _ = window.read(timeout=100)
        if event in [sg.WIN_CLOSED, '終了']:
            break
        draw_clock(canvas.Widget, datetime.datetime.now())
        window.refresh()
    window.close()

def calc_hand_coords(angle, rate):
    x = CENTER_X + CENTER_X * rate * math.cos(angle)
    y = CENTER_Y + CENTER_Y * rate * math.sin(angle)
    return x, y

def draw_hand(widget, angle, rate, width, color):
    x, y = calc_hand_coords(angle, rate)
    widget.create_line(
        CENTER_X, CENTER_Y, x, y, width=width, fill=color)

def draw_clock(widget, draw_time):
    h, m, s = draw_time.hour, draw_time.minute, draw_time.second
    h = h % 12

    widget.delete('all')
    widget.create_oval(10, 10, CENTER_X*2-10, CENTER_Y*2-10, width=2)

    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x1, y1 = calc_hand_coords(angle, 0.8)
        x2, y2 = calc_hand_coords(angle, 0.95)
        widget.create_line(x1, y1, x2, y2, width=1, fill='silver')

    h_angle = math.radians((h / 12 + m / 60 / 12) * 360 - 90)
    draw_hand(widget, h_angle, 0.5, 20, 'black')
    min_angle = math.radians((m / 60) * 360 - 90)
    draw_hand(widget, min_angle, 0.7, 15, 'black')
    sec_angle = math.radians((s / 60) * 360 - 90)
    draw_hand(widget, sec_angle, 0.9, 2, 'red')

if __name__ == '__main__':
    main()
    
