class Dino:
    """
    Class for dinosaur actions.
    """

    def __init__(self, driver):
        # instance of the driver 
        self.driver = driver
        # page element for sending keys
        self.dino = self.driver.find_element_by_class_name('offline')
    
    def up(self):
       self.dino.send_keys(u'\ue013')
    
    def down(self):
        self.dino.send_keys(u'\ue015')