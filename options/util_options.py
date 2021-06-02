from .base_options import BaseOptions


class UtilOptions(BaseOptions):
    """This class includes test options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)  # define shared options
        parser.add_argument('--extension', type=str, default='png', help='input files extension used during searching and filtering')
        parser.add_argument('--output', type=str, default='./output/', help='directory to save/copy the final files to')
        parser.add_argument('--shot_count', type=int, default=24, help='amount of images to process')
        self.isTrain = False
        return parser
