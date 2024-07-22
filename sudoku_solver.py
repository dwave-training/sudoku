# Copyright 2024 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dimod import ConstrainedQuadraticModel, Binary, quicksum
from dwave.system import LeapHybridCQMSampler

def create_variables():

    x = [[[Binary(f'{i}_{j}_{k}') for k in range(1,10)] 
                  for j in range(9)] for i in range(9)]

    return x

def build_cqm(x):

    cqm = ConstrainedQuadraticModel()
    
    # TODO: Add constraints that each row contains the numbers 1-9 exactly once




    # TODO: Add constraints that each column contains the numbers 1-9 exactly once




    # Constraints that each subsquare contains the numbers 1-9 exactly once
    subsquares = [[0,1,2],[3,4,5],[6,7,8]]
    for r in range(len(subsquares)):
        for c in range(len(subsquares)):
            for k in range(1,10):
                cqm.add_constraint(quicksum(x[i][j][k-1] for i in subsquares[r]
                                                            for j in subsquares[c]) == 1,
                                                            label=f'subsquare {r}_{c} dig {k}')
  
    
    # TODO: Add constraints that each square in the grid can only contain one digit




    return cqm

def initialize_puzzle(cqm, fixed):

    cqm.fix_variables(fixed)

    return cqm

def solve_puzzle(cqm):

    sampler = LeapHybridCQMSampler()
    sampleset = sampler.sample_cqm(cqm, label = "Training - Sudoku")

    feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)

    return feasible_sampleset.first.sample

def print_puzzle(soln):

    print("\nPuzzle Solution:\n")

    for r in range(9):
        
        msg = ''
        if r in [3,6]:
            print('  -------------------------------')

        for c in range(9):
            if c in [3,6]:
                msg += "  |"

            for d in range(1, 10):
                if soln[f'{r}_{c}_{d}'] == 1:
                    msg += "  "+str(d)

        print(msg)

if __name__ == '__main__':

    fixed = {
        '0_3_9': 1.0,
        '0_6_1': 1.0,
        '0_8_2': 1.0,
        '1_0_7': 1.0,
        '1_3_3': 1.0,
        '1_6_6': 1.0,
        '2_2_2': 1.0,
        '2_7_3': 1.0,
        '3_0_9': 1.0,
        '3_5_8': 1.0,
        '3_6_7': 1.0,
        '4_0_3': 1.0,
        '4_4_1': 1.0,
        '4_8_9': 1.0,
        '5_2_6': 1.0,
        '5_3_5': 1.0,
        '5_8_1': 1.0,
        '6_1_1': 1.0,
        '6_6_4': 1.0,
        '7_2_4': 1.0,
        '7_5_9': 1.0,
        '7_8_6': 1.0,
        '8_0_8': 1.0,
        '8_2_3': 1.0,
        '8_5_6': 1.0
    }

    x = create_variables()

    cqm = build_cqm(x)

    cqm_with_fixed = initialize_puzzle(cqm, fixed)

    soln = solve_puzzle(cqm_with_fixed)

    if soln is None:

        print("\nNo feasible solution found.")
        exit()

    print_puzzle({**soln, **fixed})
