'''
Tests for vrp package construction module
'''
import pytest

import vrp.constructive as cn
import vrp.io as io

@pytest.mark.parametrize("warehouse, selected_sectors, expected_cost", 
                         [
                          ('L51', ['L51', 'L1', 'L10', 'L100','L101'], 196.1*2),
                          ('L51', ['L51', 'L1', 'L10'], 116.7*2),
                          ('L51', ['L51', 'L1', 'L102', 'L104','L11'], 239.6*2)
                         ]
                        )
def test_capacity_one_cost(warehouse, selected_sectors, expected_cost):
    '''
    Test single occupancy cost (warehouse->city_i, city_i<-warehouse)
    '''
    matrix = io.trim_matrix(io.load_travel_distance(), selected_sectors)
    cost = cn.single_capacity_cost(warehouse, matrix)
    #allowing for minor floating point difference
    assert pytest.approx(cost) == expected_cost
    



