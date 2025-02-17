import BLL.map_execution
import BLL.abc
import BLL.control_signal

class Population:
    def __init__(self,Inbound = 0,Outbound = 0,LoadWeigth = 0,TimeStart = 0):
        if (int(Inbound) == 0 and  int(Outbound) == 0):
            self.TravelledNode = list()
            self.CostValue = float(100000)
            self.ListOfControlSignal = list()
            self.AbandonmentCounter = int(0)
            return
        self.TravelledNode = BLL.map_execution.Map.returnFeasiblePath(Inbound,Outbound)
        if (len(self.TravelledNode) >= 1):
            if(self.TravelledNode[len(self.TravelledNode) - 1] == int(Outbound)):
                self.ListOfControlSignal = BLL.control_signal.ControlSignal.returnListOfControlSignal(TimeStart,self.TravelledNode)
                self.CostValue = BLL.abc.ABC.returnCostFunction(self.ListOfControlSignal,Outbound,LoadWeigth)
                self.AbandonmentCounter = int(0)
                return
        self.CostValue = float(100000)
        self.ListOfControlSignal = list()
        self.AbandonmentCounter = int(0)