# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pycoal import mineral
import spectral
import os

def test_normalize():
    pass

def test_indexOfGreaterThan():
    """
    This tests the private method __indexOfGreaterThan in the class MineralClassification.
    Args:
        None
    Returns:
        None
    """
    test_list = [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

    # [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    #                         ---  ---
    # 6.0 is the first value greater than 5.0, so the return should be its index (6)
    assert mineral.MineralClassification._MineralClassification__indexOfGreaterThan(test_list, 5.0) == 6

    # [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    #     ---  ---
    # 2.0 is the first value greater than 1.0, so the return should be its index (2)
    assert mineral.MineralClassification._MineralClassification__indexOfGreaterThan(test_list, 1.0) == 2

    # [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    # 11.0 is not in the range of this list, so the return will just be the last index
    assert mineral.MineralClassification._MineralClassification__indexOfGreaterThan(test_list, 11.0) == 9

def test_trainClassifier():
    pass

def test_saveClassifier():
    """
    This tests the public method saveClassifier in the class MineralClassification.
    Args:
        None
    Returns:
        None
    """
    # test object
    test_obj = mineral.MineralClassification()

    # the files the test will write to
    test_dump_files = ["perceptron.p", "gaussian.p", "mahalanobi.p"]

    # create arbitrary structure for perceptron classifier
    test_struct = [9, 35, 60]

    # perceptron classifier test object
    test_perceptron = spectral.classifiers.PerceptronClassifier(test_struct)

    # dump classifier to file
    test_obj.saveClassifier(test_perceptron, test_dump_files[0])

    # assert classifier was dumped to specified file in test_dump_files
    assert os.path.isfile(test_dump_files[0])

    # gaussian classifier test object
    test_gaussian = spectral.classifiers.GaussianClassifier()

    # dump classifier to file
    test_obj.saveClassifier(test_gaussian, test_dump_files[1])

    # assert classifier was dumped to specified file in test_dump_files
    assert os.path.isfile(test_dump_files[1])

    # mahalanobi's distance classifier test object
    test_mahalanobi = spectral.classifiers.MahalanobisDistanceClassifier()

    # dump classifier to file
    test_obj.saveClassifier(test_mahalanobi, test_dump_files[2])

    # assert classifier was dumped to specified file in test_dump_files
    assert os.path.isfile(test_dump_files[2])


def test_readClassifier():
    """
    This tests the public method readClassifier in the class MineralClassification.
    Args:
        None
    Returns:
        None
    """
    # test object
    test_obj = mineral.MineralClassification()

    # the files the test will read from
    test_load_files = ["perceptron.p", "gaussian.p", "mahalanobi.p"]

    # load perceptron classifier
    test_perceptron = test_obj.readClassifier(test_load_files[0])

    # assert the object is loaded as the PerceptronClassifier type
    assert type(test_perceptron) == spectral.classifiers.PerceptronClassifier

    # assert the shape is equivalent to the shape specified in test_saveClassifier
    assert test_perceptron.shape == [9, 35, 60]

    # load gaussian classifier
    test_gaussian = test_obj.readClassifier(test_load_files[1])

    # assert the object is loaded as the GaussianClassifier type
    assert type(test_gaussian) == spectral.classifiers.GaussianClassifier

    # load mahalanobi's distance classifier
    test_mahalanobi = test_obj.readClassifier(test_load_files[2])

    # assert the object is loaded as the GaussianClassifier type
    assert type(test_mahalanobi) == spectral.classifiers.MahalanobisDistanceClassifier

    # clean up after save and read tests
    for f in test_load_files:
        os.remove(f)

def test_classifyPixel():
    pass

def test_classifyImage():
    pass

def test_classifyImages():
    pass