class Process:
    def __init__(self, name: str, pid: int):
        self.name = name
        self.pid = pid
        # self.cpu_percent = cpu_percent
        # self.power_draw = power_draw

    def __str__(self) -> str:
        return "{}: PID: {}; CPU Percent: {}; Power Draw (W): {}".format(self.name, self.pid, self.cpu_percent, self.power_draw)
    
    def get_cpu_percent(self) -> float:
        pass

    def get_power_draw(self) -> float:
        pass

class Sensors:
    def get_power_consumption() -> float:
        '''Returns the power draw of the system in Watts
        '''
        pass

    def get_process_list() -> list[Process]:
        pass