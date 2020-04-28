'''
Tests for vrp package
'''
import pytest

import vrp.io as io

@pytest.mark.parametrize("sectors, expected_shape", 
                         [
                          (['L51', 'L1', 'L10', 'L100'], (4, 4)),
                          (['L51', 'L1'], (2, 2)),
                          (['L51', 'L1', 'L102'], (3, 3))
                         ]
                        )
def test_load_and_trim_distance_matrix(sectors, expected_shape):
    '''
    Test trimmed distance matrix shape is as expected
    '''
    matrix = io.load_travel_distance()
    trimmed = io.trim_matrix(matrix, sectors)
    assert expected_shape == trimmed.shape


@pytest.mark.parametrize("sectors, expected_shape", 
                         [
                          (['L51', 'L1', 'L10', 'L100'], (4, 4)),
                          (['L51', 'L1'], (2, 2)),
                          (['L51', 'L1', 'L102'], (3, 3))
                         ]
                        )
def test_load_and_trim_time_matrix(sectors, expected_shape):
    '''
    Test trimmed time matrix shape is as expected
    '''
    matrix = io.load_travel_time()
    trimmed = io.trim_matrix(matrix, sectors)
    assert expected_shape == trimmed.shape


@pytest.mark.parametrize("sectors", 
                         [
                          (['L51', 'L1', 'L10', 'L100']),
                          (['L51', 'L1']),
                          (['L51', 'L1', 'L102'])
                         ]
                        )
def test_load_and_trim_distance_matrix_cols(sectors):
    '''
    Test trimmed distance matrix columns are as expected
    '''
    matrix = io.load_travel_distance()
    trimmed = io.trim_matrix(matrix, sectors)
    assert sectors == list(trimmed.columns)

@pytest.mark.parametrize("sectors", 
                         [
                          (['L51', 'L1', 'L10', 'L100']),
                          (['L51', 'L1']),
                          (['L51', 'L1', 'L102'])
                         ]
                        )
def test_load_and_trim_distance_matrix_rows(sectors):
    '''
    Test trimmed distance matrix rows are as expected
    '''
    matrix = io.load_travel_distance()
    trimmed = io.trim_matrix(matrix, sectors)
    assert sectors == list(trimmed.index.values)


@pytest.mark.parametrize("sectors", 
                         [
                          (['L51', 'L1', 'L10', 'L100']),
                          (['L51', 'L1']),
                          (['L51', 'L1', 'L102'])
                         ]
                        )
def test_load_and_trim_time_matrix_cols(sectors):
    '''
    Test trimmed time matrix columns are as expected
    '''
    matrix = io.load_travel_time()
    trimmed = io.trim_matrix(matrix, sectors)
    assert sectors == list(trimmed.columns)


@pytest.mark.parametrize("sectors", 
                         [
                          (['L51', 'L1', 'L10', 'L100']),
                          (['L51', 'L1']),
                          (['L51', 'L1', 'L102'])
                         ]
                        )
def test_load_and_trim_time_matrix_rows(sectors):
    '''
    Test trimmed time matrix rows are as expected
    '''
    matrix = io.load_travel_time()
    trimmed = io.trim_matrix(matrix, sectors)
    assert sectors == list(trimmed.index.values)


@pytest.mark.parametrize("city_1, city_2, expected_cost", 
                        [
                         (0, 1, 113.4),
                         (1, 0, 113.4),
                         (1, 3, 80.2),
                         (3, 1, 80.2),
                         (2, 4, 27.9),
                         (4, 2, 27.9),
                         ('L1', 'L10', 113.4),
                         ('L10', 'L1', 113.4),
                         ('L10', 'L100', 33.0),
                         ('L100', 'L10', 33.0),
                         ('L100', 'L102', 27.9),
                         ('L102', 'L100', 27.9)
                        ])
def test_travel_distance_cost(city_1, city_2, expected_cost):
    '''
    Test costs are symmetric.
    '''
    df = io.load_travel_distance()
    sectors = ['L1', 'L10', 'L100','L101', 'L102']
    trimmed = io.trim_matrix(df, sectors)
    print(trimmed)
    cost = io.travel_cost(city_1, city_2, trimmed)
    assert expected_cost == cost