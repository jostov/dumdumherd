from sklearn.naive_bayes import GaussianNB
from random import shuffle, choice

class DumDumHerd(object):

  def __init__(self):
    self.the_herd = []
    self.herdsize = 0
    pass

  def fit(self, features, class_labels):
    train_dict = {}

    for each in zip(class_labels, features):
      if each[0] not in train_dict:
       train_dict[each[0]] = []
      train_dict[each[0]].append(each[1])

    for each in train_dict:
     shuffle(train_dict[each])
    
    self.herdsize = len(train_dict[train_dict.keys()[0]])
    for i in range(self.herdsize):
      training_subset = [[],[]]
      for each in train_dict:
        training_subset[0].append(each)
        training_subset[1].append(train_dict[each].pop())
      new_dumdum = GaussianNB()
      new_dumdum.fit(training_subset[1], training_subset[0])
      self.the_herd.append(new_dumdum)
  def predict(self, vector):
    votes = {}
    for each in self.the_herd:
      vote = each.predict(vector)[0]
      if vote not in votes:
        votes[vote] = 1
      else:
        votes[vote] += 1

    prev = [0, None]
    for each in votes:
      if votes[each] >= prev[0]:
        prev[1] = each
        prev[0] = votes[each]
    return prev[1]







