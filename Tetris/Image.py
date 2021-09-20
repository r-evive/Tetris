import pygame;
from Resource import *;
class Image(object):

    def __init__(self,screen):
        self.__screen = screen;
        self.background_Image = pygame.image.load(Resource.createPath("Images\\background.png")).convert_alpha();
        self.logo_Image = pygame.image.load(Resource.createPath("Images\\logo.png")).convert_alpha();
        self.start_off_Image =pygame.image.load( Resource.createPath("Images\\start_off.png")).convert_alpha();
        self.resume_off_Image = pygame.image.load(Resource.createPath("Images\\resume_off.png")).convert_alpha();
        self.exit_off_Image = pygame.image.load(Resource.createPath("Images\\exit_off.png")).convert_alpha();
        self.exit_on_Image = pygame.image.load(Resource.createPath("Images\\exit_on.png")).convert_alpha();
        self.start_on_Image = pygame.image.load(Resource.createPath("Images\\start_on.png")).convert_alpha();
        self.options_off_Image = pygame.image.load(Resource.createPath("Images\\options_off.png")).convert_alpha();
        self.options_on_Image = pygame.image.load(Resource.createPath("Images\\options_on.png")).convert_alpha();
        self.ranking_off_Image = pygame.image.load(Resource.createPath("Images\\ranking_off.png")).convert_alpha();
        self.ranking_on_Image = pygame.image.load(Resource.createPath("Images\\ranking_on.png")).convert_alpha();
        self.textInput_Image = pygame.image.load(Resource.createPath("Images\\textInput.png")).convert_alpha();
        self.next_on_Image = pygame.image.load(Resource.createPath("Images\\next_on.png")).convert_alpha();
        self.next_off_Image = pygame.image.load(Resource.createPath("Images\\next_off.png")).convert_alpha();
        self.board_Image = pygame.image.load(Resource.createPath("Images\\board.png")).convert_alpha();
        self.points_Image = pygame.image.load(Resource.createPath("Images\\points.png")).convert_alpha();
        self.nextBlocks_Image = pygame.image.load(Resource.createPath("Images\\nextBlocks.png")).convert_alpha();
        self.redBlock_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\redBlock.png")).convert_alpha();
        self.yellowBlock_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\yellowBlock.png")).convert_alpha();
        self.greenBlock_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\greenBlock.png")).convert_alpha();
        self.pinkBlock_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\pinkBlock.png")).convert_alpha();
        self.orangeBlock_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\orangeBlock.png")).convert_alpha();
        self.purpleBlock_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\purpleBlock.png")).convert_alpha();
        self.blueBlock_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\blueBlock.png")).convert_alpha();
        self.redBlockPreview_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\redBlockPreview.png")).convert_alpha();
        self.yellowBlockPreview_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\yellowBlockPreview.png")).convert_alpha();
        self.greenBlockPreview_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\greenBlockPreview.png")).convert_alpha();
        self.pinkBlockPreview_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\pinkBlockPreview.png")).convert_alpha();
        self.orangeBlockPreview_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\orangeBlockPreview.png")).convert_alpha();
        self.purpleBlockPreview_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\purpleBlockPreview.png")).convert_alpha();
        self.blueBlockPreview_Texture = pygame.image.load(Resource.createPath("Images\\Blocks\\blueBlockPreview.png")).convert_alpha();
        self.boardBackground = pygame.image.load(Resource.createPath("Images\\boardBackground.png")).convert_alpha();
        self.rankingImage = pygame.image.load(Resource.createPath("Images\\rankingImage.png")).convert_alpha();
        self.rankingListElementOff = pygame.image.load(Resource.createPath("Images\\rankingListElementOff.png")).convert_alpha();
        self.rankingListElementOn = pygame.image.load(Resource.createPath("Images\\rankingListElementOn.png")).convert_alpha();
        self.backButtonOff = pygame.image.load(Resource.createPath("Images\\back_Off.png")).convert_alpha();
        self.backButtonOn = pygame.image.load(Resource.createPath("Images\\back_On.png")).convert_alpha();
        self.blowUpTestImage = pygame.image.load(Resource.createPath("Images\\blowuptest.png")).convert_alpha();