import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.original = []
        self.all = kwargs
        for key, value in kwargs.items():
            self.original.extend([key] * value)
        self.reset()


    def reset(self):
        self.contents = copy.copy(self.original)


    def draw(self, num_balls_drawn):
        contentsLength = len(self.contents)
        if num_balls_drawn > contentsLength:
            num_balls_drawn = contentsLength
        
        balls = []
        for i in range(num_balls_drawn):
            balls.append(self.drawOne())

        return balls


    def drawOne(self):
        return self.contents.pop(random.randint(0, len(self.contents) - 1))


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    numMatched = 0
    for i in range(num_experiments):
        ballsList = hat.draw(num_balls_drawn)
        balls = {}
        for ball in ballsList:
            balls[ball] = balls.get(ball, 0) + 1

        # print('draw', i, expected_balls, balls) #DEBUG

        matched = True
        for k, v in expected_balls.items():
            if balls.get(k, 0) < v:
                # print('unmatch', k, 'drawn', balls.get(k, 0), 'expected', v) #DEBUG
                matched = False
                break

        if matched:
            numMatched += 1
            # print('matched') #DEBUG

        hat.reset()
    
    return numMatched / num_experiments
