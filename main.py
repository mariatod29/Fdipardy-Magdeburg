import  GUI as g
import buzzer as b
import multiprocessing as mp

if __name__ == '__main__':

    p2 = mp.Process(target=b.start_buzzer, args=())
    p1 = mp.Process(target=g.start_gui, args=())
    p2.start()
    p1.start()