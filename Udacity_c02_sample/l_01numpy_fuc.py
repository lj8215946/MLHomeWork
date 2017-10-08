# Use the numpy library
import numpy as np


def prepare_inputs(inputs):
    # create a 2-dimensional ndarray from the given 1-dimensional list;
    #       assign it to input_array
    output_array = np.array([inputs])

    # find the minimum value in input_array and subtract that
    #       value from all the elements of input_array. Store the
    #       result in inputs_minus_min

    outputs_minus_min = output_array - np.min(output_array)

    # find the maximum value in inputs_minus_min and divide
    #       all of the values in inputs_minus_min by the maximum value.
    #       Store the results in inputs_div_max.
    max_value = outputs_minus_min.max()
    outputs_div_max = outputs_minus_min/max_value

    # return the three arrays we've created
    return output_array, outputs_minus_min, outputs_div_max


def multiply_inputs(m1, m2):
    # Check the shapes of the matrices m1 and m2.
    #       m1 and m2 will be ndarray objects.
    #
    #       Return False if the shapes cannot be used for matrix
    #       multiplication. You may not use a transpose
    if type(m1) != np.ndarray or type(m2) != np.ndarray or m1.ndim != 2 or m2.ndim != 2 \
            or m1.shape[1] != m2.shape[0] and m1.shape[0] != m2.shape[1]:
        return False

    # If you have not returned False, then calculate the matrix product
    #       of m1 and m2 and return it. Do not use a transpose,
    #       but you swap their order if necessary
    if m1.shape[1] == m2.shape[0]:
        return m1.dot(m2)
    else:
        return m2.dot(m1)


def find_mean(values):
    #  Return the average of the values in the given Python list
    np_array_values = np.array(values)
    return np_array_values.mean()


input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1, 2, 7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

print("Multiply 1:\n{}".format(multiply_inputs(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1], [2], [3], [4]]))))
print("Multiply 2:\n{}".format(multiply_inputs(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1], [2], [3]]))))
print("Multiply 3:\n{}".format(multiply_inputs(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1, 2]]))))

print("Mean == {}".format(find_mean([1, 3, 4])))
