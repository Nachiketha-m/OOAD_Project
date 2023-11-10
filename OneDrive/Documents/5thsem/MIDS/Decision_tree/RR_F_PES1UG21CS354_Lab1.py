"""
    Assume input tensor is of the form:
    tensor = [outlook,temp,humidity,windy,play]
    here play is the target variable (class)
    remaining four are explanatory variables

"""
import torch
import math

"""Calculate the entropy of the entire dataset"""
# input:tensor
# output:int/float
def get_entropy_of_dataset(tensor: torch.Tensor):
  """
    Assume input tensor is of the form:
    tensor = [outlook,temp,humidity,windy,play]
    here play is the target variable (class)
    remaining four are explanatory variables

  """

  n_samples = tensor.shape[0]

  unique = tensor[:, -1].unique()

  entropy = 0

  for value in unique:
    n_samples_with_value = (tensor[:, -1] == value).sum()

    p_value = n_samples_with_value / n_samples

    entropy -= p_value * math.log2(p_value)#adding entropy

  return entropy
  pass


"""Return avg_info of the attribute provided as parameter"""

def get_avg_info_of_attribute(tensor:torch.Tensor, attribute:int)-> int:
    # TODO
    
    num_samples = len(tensor)
    if num_samples == 0:
        return 0

    unique = torch.unique(tensor[:, attribute])
    avg_info = 0

    for value in unique:
        subset_mask = tensor[:, attribute] == value
        subset = tensor[subset_mask]
        subset_size = len(subset)
        subset_entropy = get_entropy_of_dataset(subset)

        avg_info += (subset_size / num_samples) * subset_entropy

    return avg_info
    pass



"""Return Information Gain of the attribute provided as parameter"""
# input:tensor,attribute number
# output:int/float
def get_information_gain(tensor:torch.Tensor, attribute:int)-> float:
    entropy_dataset = get_entropy_of_dataset(tensor)
    avg_info_attribute = get_avg_info_of_attribute(tensor, attribute)
    
    information_gain = entropy_dataset - avg_info_attribute
    return information_gain
    # TODO
    pass



# input: tensor
# output: ({dict},int)
def get_selected_attribute(tensor:torch.Tensor)->int:
    """
    Return a tuple with the first element as a dictionary which has IG of all columns
    and the second element as an integer representing attribute number of selected attribute

    example : ({0: 0.123, 1: 0.768, 2: 1.23} , 2)
    """
    # TODO
    num_attributes = tensor.shape[1] - 1  # Exclude the target column
    information_gains = {}

    for attribute in range(num_attributes):
        information_gain = get_information_gain(tensor, attribute)
        information_gains[attribute] = information_gain

    selected_attribute = max(information_gains, key=information_gains.get)
    return information_gains, selected_attribute
    pass

