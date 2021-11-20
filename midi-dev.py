import pygame.midi as m
def main():
    m.init()
    i_num = m.get_count()
    for i in range(i_num):
        print(i)
        print(m.get_device_info(i))
    m.quit()
    exit()

if __name__=="__main__":
    main()
