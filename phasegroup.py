import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

plt.rcParams["figure.figsize"] = [11, 7]
fig, (ax1, ax2, ax3) = plt.subplots(3,1)
fig.suptitle('Prędkość fazowa oraz prędkość grupowa', fontsize=16)
ax1.set_title('f1(x)')
ax2.set_title('f2(x)')
ax3.set_title('f1(x)+f2(x)')
ax3.set_xlabel('Czerwona kropka to prędkość fazowa, a niebieska kropka to prędkość grupowa \n Zatrzymanie animacji przy użyciu spacji, a zrzut ekranu klikając "S"')

line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')
line3, = ax3.plot([], [], lw=2, color='c')
dot, = ax3.plot([], [], 'o', color='red')
dot2, = ax3.plot([], [], 'o', color='blue')

line = [line1, line2, line3, dot, dot2]
x = np.linspace(0, 10, 1000)

axw1 = plt.axes([0.92, 0.2, 0.0225, 0.63])
w1_slider = Slider(
    ax=axw1,
    label='w1',
    valmin=0,
    valmax=3,
    valinit=0.05,
    orientation="vertical"
)

axw2 = plt.axes([0.96, 0.2, 0.0225, 0.63])
w2_slider = Slider(
    ax=axw2,
    label='w2',
    valmin=0,
    valmax=3,
    valinit=0.04,
    orientation="vertical"
)

axk1 = plt.axes([0.02, 0.2, 0.0225, 0.63])
k1_slider = Slider(
    ax=axk1,
    label="k1",
    valmin=0,
    valmax=3,
    valinit=1.2,
    orientation="vertical"
)

axk2 = plt.axes([0.06, 0.2, 0.0225, 0.63])
k2_slider = Slider(
    ax=axk2,
    label="k2",
    valmin=0,
    valmax=3,
    valinit=1.1,
    orientation="vertical"
)

for ax in [ax1, ax2, ax3]:
    ax.set_ylim(-2.2, 2.2)
    ax.set_xlim(0, 10)



def run_animation():
    anim_running = True

    def onClick(event):
        nonlocal anim_running
        if anim_running:

            ani.event_source.stop()
            anim_running = False
        else:

            ani.event_source.start()
            anim_running = True

    fig.canvas.mpl_connect("key_press_event", onClick)

    def run(i):

        y = np.cos(2 * np.pi * (w1_slider.val * i - x * k1_slider.val))
        line[0].set_data(x, y)
        y1 = np.cos(2 * np.pi * (w2_slider.val * i - x * k2_slider.val))
        line[1].set_data(x, y1)
        y2 = y1 + y
        line[2].set_data(x, y2)
        dot.set_data(((w1_slider.val + w2_slider.val) * i) / (k1_slider.val + k2_slider.val), 2 * np.cos(2 * np.pi * (
                    (w1_slider.val - w2_slider.val) * i - ((w1_slider.val + w2_slider.val) * i) / (
                        k1_slider.val + k2_slider.val) * (k1_slider.val - k2_slider.val)) / 2))
        dot2.set_data(((w1_slider.val - w2_slider.val) * i) / (k1_slider.val - k2_slider.val), 2)
        return line


    ani = animation.FuncAnimation(fig, run, frames=2000, blit=True, interval=10, repeat=True)

resetax = plt.axes([0.87, 0.02, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    w1_slider.reset()
    k1_slider.reset()
    w2_slider.reset()
    k2_slider.reset()

button.on_clicked(reset)

run_animation()
plt.show()
