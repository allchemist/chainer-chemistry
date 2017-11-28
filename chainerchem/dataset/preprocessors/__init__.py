# from chainerchem.dataset.preprocessors import base_preprocessor  # NOQA
# from chainerchem.dataset.preprocessors import ggnn_preprocessor  # NOQA
# from chainerchem.dataset.preprocessors import mol_preprocessor  # NOQA
# from chainerchem.dataset.preprocessors import nfp_preprocessor  # NOQA


from chainerchem.dataset.preprocessors.atomic_number_preprocessor import AtomicNumberPreprocessor  # NOQA
from chainerchem.dataset.preprocessors.base_preprocessor import BasePreprocessor  # NOQA
from chainerchem.dataset.preprocessors.common import get_atomic_numbers  # NOQA
from chainerchem.dataset.preprocessors.common import type_check_num_atoms  # NOQA
from chainerchem.dataset.preprocessors.ggnn_preprocessor import GGNNPreprocessor  # NOQA
from chainerchem.dataset.preprocessors.mol_preprocessor import ECFPPreprocessor  # NOQA
from chainerchem.dataset.preprocessors.mol_preprocessor import MolFeatureExtractFailure  # NOQA
from chainerchem.dataset.preprocessors.mol_preprocessor import MolPreprocessor  # NOQA
from chainerchem.dataset.preprocessors.nfp_preprocessor import NFPPreprocessor  # NOQA
from chainerchem.dataset.preprocessors.schnet_preprocessor import SchNetPreprocessor  # NOQA
from chainerchem.dataset.preprocessors.weavenet_preprocessor import WeaveNetPreprocessor  # NOQA

preprocess_method_dict = {
    'ecfp': ECFPPreprocessor,
    'nfp': NFPPreprocessor,
    'ggnn': GGNNPreprocessor,
    'schnet': SchNetPreprocessor,
    'weavenet': WeaveNetPreprocessor,
}
