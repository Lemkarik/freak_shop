from interface_setup import *
import time
import enum


class ReturnStatus(enum.Enum):
    stay = 0
    quit = 1
    register = 2
    login = 3
    go_to_login = 4
    go_to_register = 5
    start_game = 6
    leaderboard = 7


class MenuView:
    def __init__(self):
        self.lang = Languages.russian
        self.reset_menu_language(self.lang)

        self.EnterButtonInitial = Rect(ScreenWidth * 11 / 38, ScreenHeight / 6, 800, 250)
        self.RegistrationButtonInitial = Rect(ScreenWidth * 11 / 38, ScreenHeight / 2, 800, 250)
        self.BackButtonInitial = Rect(ScreenWidth * 6 / 7, ScreenHeight * 1 / 30, 180, 180)

        self.LoginButtonLogin = Rect(ScreenWidth * 5 / 38, ScreenHeight / 5, 1000, 150)
        self.PasswordButtonLogin = Rect(ScreenWidth * 5 / 38, ScreenHeight * 6 / 10, 1000, 150)
        self.ConfirmButtonLogin = Rect(ScreenWidth * 27 / 38, ScreenHeight / 3 - 40, 400, 400)
        self.EyeIconButtonLogin = Rect(ScreenWidth / 80, ScreenHeight * 6 / 10 - 20, 220, 180)

        self.LoginButtonRegistration = Rect(ScreenWidth * 5 / 38, ScreenHeight / 12 + 20, 1000, 150)
        self.NicknameButtonRegistration = Rect(ScreenWidth * 5 / 38, ScreenHeight / 4 + 60, 1000, 150)
        self.PasswordButtonRegistration = Rect(ScreenWidth * 5 / 38, ScreenHeight / 2 + 20, 1000, 150)
        self.RepeatPasswordButtonRegistration = Rect(ScreenWidth * 5 / 38, ScreenHeight * 7 / 10 + 40, 1000, 150)
        self.ConfirmButtonRegistration = Rect(ScreenWidth * 27 / 38, ScreenHeight / 3 - 40, 400, 400)
        self.EyeIconButton1 = Rect(ScreenWidth / 80, ScreenHeight / 2 - 20, 220, 180)
        self.EyeIconButton2 = Rect(ScreenWidth / 80, ScreenHeight * 7 / 10 - 20, 220, 180)

        self.JoinGameButton = Rect(ScreenWidth * 10 / 38, ScreenHeight / 20 + 40, 850, 200)
        self.CreateGameButton = Rect(ScreenWidth * 10 / 38, ScreenHeight / 4 + 40, 850, 200)
        self.SettingsButton = Rect(ScreenWidth * 10 / 38, ScreenHeight * 4 / 9 + 45, 850, 200)
        self.RankingsButton = Rect(ScreenWidth * 10 / 38, ScreenHeight * 2 / 3 + 25, 850, 200)

        self.BackIconImage = pygame.image.load("src/img/BackIcon.png").convert_alpha()
        self.EyeIconImage = pygame.image.load("src/img/EyeIcon.png").convert_alpha()
        self.EyeIconImageCrossed = pygame.image.load("src/img/EyeIconCrossed.png").convert_alpha()

        self.ReturnToMenu = 0
        self.LoginInput = ""
        self.PasswordInput = ""
        self.RepeatPasswordInput = ""
        self.NicknameInput = ""
        self.active = 0
        self.password_show = False
        self.repeat_password_show = False

    def reset_menu_info(self):
        self.ReturnToMenu = 0
        self.LoginInput = ""
        self.PasswordInput = ""
        self.RepeatPasswordInput = ""
        self.NicknameInput = ""
        self.active = 0
        self.password_show = False
        self.repeat_password_show = False

        # Changing the language of all menus
    def reset_menu_language(self,new_lang):
        self.LoginText = RegistrationFont.render(LoginTexts[new_lang], False, (0, 0, 0))
        self.NicknameText = RegistrationFont.render(NicknameTexts[new_lang], False, (0, 0, 0))
        self.PasswordText = RegistrationFont.render(PasswordTexts[new_lang], False, (0, 0, 0))
        self.RepeatPasswordText = RegistrationFont.render(RepeatPasswordTexts[new_lang], False, (0, 0, 0))
        self.ConfirmTextLogin = RegistrationFont.render(ConfirmTexts[new_lang], False, (0, 0, 0))
        self.ConfirmTextRegistration = RegistrationFont.render(RegistrationTexts[new_lang], False, (0, 0, 0))

        self.LoginTextInitial = RegistrationFont.render(ConfirmTexts[new_lang], False, (0, 0, 0))
        self.RegistrationTextInitial = RegistrationFont.render(InitialRegistrationTexts[new_lang], False, (0, 0, 0))
        self.BackButton = Rect(ScreenWidth * 6 / 7, ScreenHeight * 1 / 30, 180, 180)

        self.JoinGameText = RegistrationFont.render(JoinGameTexts[new_lang], False, (0, 0, 0))
        self.CreateGameText = RegistrationFont.render(CreateGameTexts[new_lang], False, (0, 0, 0))
        self.SettingsText = RegistrationFont.render(SettingsTexts[new_lang], False, (0, 0, 0))
        self.RankingsText = RegistrationFont.render(LeaderbordTexts[new_lang], False, (0, 0, 0))

    def show_login_menu(self):
        screen.fill(RegistrationBackgroundColor)
        for event in pygame.event.get():
            if event.type == QUIT:
                Returnee = [ReturnStatus.quit, [""]]
                return Returnee
            if event.type == MOUSEBUTTONDOWN:
                MousePosition = pygame.mouse.get_pos()
                if self.LoginButtonLogin.collidepoint(MousePosition):
                    self.active = 1
                elif self.PasswordButtonLogin.collidepoint(MousePosition):
                    self.active = 2
                elif self.ConfirmButtonLogin.collidepoint(MousePosition):
                    self.active = 0
                    Returnee = [ReturnStatus.login, [self.LoginInput, self.PasswordInput]]
                    return Returnee
                elif self.EyeIconButtonLogin.collidepoint(MousePosition):
                    self.password_show = not self.password_show
                elif self.BackButton.collidepoint(MousePosition):
                    Returnee = [ReturnStatus.quit, [""]]
                    return Returnee
                else:
                    self.active = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Returnee = [ReturnStatus.quit, [""]]
                    return Returnee
                elif event.key == K_DOWN:
                    self.active += 1 * (self.active < 2)
                elif event.key == K_UP:
                    self.active -= 1 * (self.active > 1)
                else:
                    if self.active == 1:
                        if event.key == K_BACKSPACE:
                            self.LoginInput = self.LoginInput[:-1]
                        elif event.key == K_RETURN:
                            self.active = 2
                        elif len(self.LoginInput) < MaxLoginLength:
                            self.LoginInput += event.unicode
                    elif self.active == 2:
                        if event.key == K_BACKSPACE:
                            self.PasswordInput = self.PasswordInput[:-1]
                        elif event.key == K_RETURN:
                            self.active = 0
                        elif len(self.PasswordInput) < MaxPasswordLength:
                            self.PasswordInput += event.unicode
                    if self.active == 0:
                        if event.key == K_RETURN:
                            Returnee = [ReturnStatus.login, [self.LoginInput, self.PasswordInput]]
                            return Returnee

        pygame.draw.rect(screen, RegistrationButtonColor, self.LoginButtonLogin)
        pygame.draw.rect(screen, RegistrationButtonColor, self.PasswordButtonLogin)
        pygame.draw.rect(screen, RegistrationButtonColor, self.ConfirmButtonLogin)
        screen.blit(self.LoginText, (self.LoginButtonLogin.midtop[0] - 100, self.LoginButtonLogin.midtop[1] - 80))
        screen.blit(self.PasswordText,
                    (self.PasswordButtonLogin.midtop[0] - 120, self.PasswordButtonLogin.midtop[1] - 80))
        screen.blit(self.ConfirmTextLogin,
                    (self.ConfirmButtonLogin.center[0] - 85, self.ConfirmButtonLogin.center[1] - 30))

        LoginInputText = RegistrationFont.render(self.LoginInput + (self.active == 1) * '|', False, (0, 0, 0))
        screen.blit(LoginInputText, (self.LoginButtonLogin.left, self.LoginButtonLogin.center[1] - 35))

        if self.password_show:
            screen.blit(pygame.transform.scale(self.EyeIconImage, (220, 180)),
                        (ScreenWidth / 80, ScreenHeight * 6 / 10 - 20))
            PasswordInputText = RegistrationFont.render(self.PasswordInput + (self.active == 2) * '|', False, (0, 0, 0))
            screen.blit(PasswordInputText, (self.PasswordButtonLogin.left, self.PasswordButtonLogin.center[1] - 35))
        else:
            screen.blit(pygame.transform.scale(self.EyeIconImageCrossed, (250, 160)),
                        (ScreenWidth / 80 - 10, ScreenHeight * 6 / 10 - 10))
            PasswordInputText = RegistrationFont.render('*' * len(self.PasswordInput) + (self.active == 2) * '|', False,
                                                        (0, 0, 0))
            screen.blit(PasswordInputText, (self.PasswordButtonLogin.left, self.PasswordButtonLogin.center[1] - 10))
        screen.blit(pygame.transform.scale(self.BackIconImage, (180, 180)),
                    (ScreenWidth * 6 / 7, ScreenHeight * 1 / 30))

        Returnee = [ReturnStatus.stay, [""]]
        return Returnee

    def show_resgistration_menu(self):
        screen.fill(RegistrationBackgroundColor)
        for event in pygame.event.get():
            if event.type == QUIT:
                Returnee = [ReturnStatus.quit, [""]]
                return Returnee
            if event.type == MOUSEBUTTONDOWN:
                MousePosition = pygame.mouse.get_pos()
                if self.LoginButtonRegistration.collidepoint(MousePosition):
                    self.active = 1
                elif self.NicknameButtonRegistration.collidepoint(MousePosition):
                    self.active = 2
                elif self.PasswordButtonRegistration.collidepoint(MousePosition):
                    self.active = 3
                elif self.RepeatPasswordButtonRegistration.collidepoint(MousePosition):
                    self.active = 4
                elif self.ConfirmButtonRegistration.collidepoint(MousePosition):
                    Returnee = [ReturnStatus.register,[self.LoginInput, self.NicknameInput, self.PasswordInput,
                                                                      self.RepeatPasswordInput]]
                    return Returnee
                elif self.EyeIconButton1.collidepoint(MousePosition):
                    self.password_show = not self.password_show
                elif self.EyeIconButton2.collidepoint(MousePosition):
                    self.repeat_password_show = not self.repeat_password_show
                elif self.BackButton.collidepoint(MousePosition):
                    Returnee = [ReturnStatus.quit, [""]]
                    return Returnee
                else:
                    self.active = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Returnee = [ReturnStatus.quit, [""]]
                    return Returnee
                elif event.key == K_DOWN:
                    self.active += 1 * (self.active < 4)
                elif event.key == K_UP:
                    self.active -= 1 * (self.active > 1)
                else:
                    if self.active == 1:
                        if event.key == K_BACKSPACE:
                            self.LoginInput = self.LoginInput[:-1]
                        elif event.key == K_RETURN:
                            self.active = 2
                        elif len(self.LoginInput) < MaxLoginLength:
                            self.LoginInput += event.unicode
                    elif self.active == 2:
                        if event.key == K_BACKSPACE:
                            self.NicknameInput = self.NicknameInput[:-1]
                        elif event.key == K_RETURN:
                            self.active = 3
                        elif len(self.NicknameInput) < MaxPasswordLength:
                            self.NicknameInput += event.unicode
                    elif self.active == 3:
                        if event.key == K_BACKSPACE:
                            self.PasswordInput = self.PasswordInput[:-1]
                        elif event.key == K_RETURN:
                            self.active = 4
                        elif len(self.PasswordInput) < MaxPasswordLength:
                            self.PasswordInput += event.unicode
                    elif self.active == 4:
                        if event.key == K_BACKSPACE:
                            self.RepeatPasswordInput = self.RepeatPasswordInput[:-1]
                        elif event.key == K_RETURN:
                            self.active = 0
                        elif len(self.RepeatPasswordInput) < MaxPasswordLength:
                            self.RepeatPasswordInput += event.unicode
                    if self.active == 0:
                        if event.key == K_RETURN:
                            Returnee = [ReturnStatus.register,
                                        [self.LoginInput, self.NicknameInput, self.PasswordInput,
                                         self.RepeatPasswordInput]]
                            return Returnee

        pygame.draw.rect(screen, RegistrationButtonColor, self.LoginButtonRegistration)
        pygame.draw.rect(screen, RegistrationButtonColor, self.NicknameButtonRegistration)
        pygame.draw.rect(screen, RegistrationButtonColor, self.PasswordButtonRegistration)
        pygame.draw.rect(screen, RegistrationButtonColor, self.RepeatPasswordButtonRegistration)
        pygame.draw.rect(screen, RegistrationButtonColor, self.ConfirmButtonRegistration)
        screen.blit(self.LoginText, (self.LoginButtonRegistration.midtop[0] - 100, self.LoginButtonRegistration.midtop[1] - 80))
        screen.blit(self.NicknameText, (self.NicknameButtonRegistration.midtop[0] - 80, self.NicknameButtonRegistration.midtop[1] - 60))
        screen.blit(self.PasswordText, (self.PasswordButtonRegistration.midtop[0] - 120, self.PasswordButtonRegistration.midtop[1] - 60))
        screen.blit(self.RepeatPasswordText, (self.RepeatPasswordButtonRegistration.midtop[0] - 220, self.RepeatPasswordButtonRegistration.midtop[1] - 60))
        screen.blit(self.ConfirmTextRegistration, (self.ConfirmButtonRegistration.center[0] - 180, self.ConfirmButtonRegistration.center[1] - 20))

        LoginInputText = RegistrationFont.render(self.LoginInput + (self.active == 1) * '|', False, (0, 0, 0))
        NicknameInputText = RegistrationFont.render(self.NicknameInput + (self.active == 2) * '|', False, (0, 0, 0))
        screen.blit(LoginInputText, (self.LoginButtonRegistration.left, self.LoginButtonRegistration.center[1] - 35))
        screen.blit(NicknameInputText, (self.NicknameButtonRegistration.left, self.NicknameButtonRegistration.center[1] - 35))

        if self.password_show:
            screen.blit(pygame.transform.scale(self.EyeIconImage, (220, 180)),
                        (ScreenWidth / 80, ScreenHeight / 2 + 10))
            PasswordInputText = RegistrationFont.render(self.PasswordInput + (self.active == 3) * '|', False, (0, 0, 0))
            screen.blit(PasswordInputText, (self.PasswordButtonRegistration.left, self.PasswordButtonRegistration.center[1] - 35))
        else:
            screen.blit(pygame.transform.scale(self.EyeIconImageCrossed, (250, 160)),
                        (ScreenWidth / 80 - 10, ScreenHeight / 2 + 20))
            PasswordInputText = RegistrationFont.render('*' * len(self.PasswordInput) + (self.active == 3) * '|', False,
                                                        (0, 0, 0))
            screen.blit(PasswordInputText, (self.PasswordButtonRegistration.left, self.PasswordButtonRegistration.center[1] - 10))

        if self.repeat_password_show:
            screen.blit(pygame.transform.scale(self.EyeIconImage, (220, 180)),
                        (ScreenWidth / 80, ScreenHeight * 7 / 10 + 20))
            RepeatPasswordInputText = RegistrationFont.render(self.RepeatPasswordInput + (self.active == 4) * '|', False,
                                                              (0, 0, 0))
            screen.blit(RepeatPasswordInputText, (self.RepeatPasswordButtonRegistration.left, self.RepeatPasswordButtonRegistration.center[1] - 35))
        else:
            screen.blit(pygame.transform.scale(self.EyeIconImageCrossed, (250, 160)),
                        (ScreenWidth / 80 - 10, ScreenHeight * 7 / 10 + 30))
            RepeatPasswordInputText = RegistrationFont.render('*' * len(self.RepeatPasswordInput) + (self.active == 4) * '|',
                                                              False, (0, 0, 0))
            screen.blit(RepeatPasswordInputText, (self.RepeatPasswordButtonRegistration.left, self.RepeatPasswordButtonRegistration.center[1] - 10))
        screen.blit(pygame.transform.scale(self.BackIconImage, (180, 180)),
                    (ScreenWidth * 6 / 7, ScreenHeight * 1 / 30))

        Returnee = [ReturnStatus.stay, [""]]
        return Returnee

    def show_start_menu(self):
        screen.fill(RegistrationBackgroundColor)
        for event in pygame.event.get():
            if event.type == QUIT:
                Returnee = [ReturnStatus.quit, [""]]
                return Returnee
            if event.type == MOUSEBUTTONDOWN:
                if self.EnterButtonInitial.collidepoint(pygame.mouse.get_pos()):
                    Returnee = [ReturnStatus.go_to_login, [""]]
                    return Returnee
                elif self.RegistrationButtonInitial.collidepoint(pygame.mouse.get_pos()):
                    Returnee = [ReturnStatus.go_to_register, [""]]
                    return Returnee
                elif self.BackButton.collidepoint(pygame.mouse.get_pos()):
                    Returnee = [ReturnStatus.quit, [""]]
                    return Returnee
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_ESCAPE]:
            Returnee = [ReturnStatus.quit, [""]]
            return Returnee
        pygame.draw.rect(screen, RegistrationButtonColor, self.EnterButtonInitial)
        pygame.draw.rect(screen, RegistrationButtonColor, self.RegistrationButtonInitial)
        screen.blit(pygame.transform.scale(self.BackIconImage, (180, 180)),
                    (ScreenWidth * 6 / 7, ScreenHeight * 1 / 30))
        screen.blit(self.LoginTextInitial,
                    (self.EnterButtonInitial.center[0] - 85, self.EnterButtonInitial.center[1] - 40))
        screen.blit(self.RegistrationTextInitial,
                    (self.RegistrationButtonInitial.center[0] - 285, self.RegistrationButtonInitial.center[1] - 40))

        Returnee = [ReturnStatus.stay, [""]]
        return Returnee

    def show_main_menu(self):
        screen.fill(RegistrationBackgroundColor)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.JoinGameButton.collidepoint(pygame.mouse.get_pos()):
                    Returnee = [ReturnStatus.start_game, [""]]
                    return Returnee
                elif self.BackButton.collidepoint(pygame.mouse.get_pos()):
                    Returnee = [ReturnStatus.quit, [""]]
                    return Returnee
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_ESCAPE]:
            sys.exit()
        pygame.draw.rect(screen, RegistrationButtonColor, self.JoinGameButton)
        pygame.draw.rect(screen, RegistrationButtonColor, self.CreateGameButton)
        pygame.draw.rect(screen, RegistrationButtonColor, self.SettingsButton)
        pygame.draw.rect(screen, RegistrationButtonColor, self.RankingsButton)
        screen.blit(self.JoinGameText, (self.JoinGameButton.center[0] - 325, self.JoinGameButton.center[1] - 35))
        screen.blit(self.CreateGameText, (self.CreateGameButton.center[0] - 185, self.CreateGameButton.center[1] - 35))
        screen.blit(self.SettingsText, (self.SettingsButton.center[0] - 150, self.SettingsButton.center[1] - 35))
        screen.blit(self.RankingsText, (self.RankingsButton.center[0] - 230, self.RankingsButton.center[1] - 35))
        screen.blit(pygame.transform.scale(self.BackIconImage, (180, 180)),
                    (ScreenWidth * 6 / 7, ScreenHeight * 1 / 30))
        Returnee = [ReturnStatus.stay, [""]]
        return Returnee

    def show_message(self, message):
        MessageRect = Rect(ScreenWidth / 2 - (100 + len(message) * 15), ScreenHeight / 4 + 50,
                           220 + len(message) * 30, 350)
        pygame.draw.rect(screen, MessageBackgroundColor, MessageRect)
        MessageText = RegistrationFont.render(message, False, (0, 0, 0))
        screen.blit(MessageText,
                    (MessageRect.center[0] - (10 + len(message) * 15), MessageRect.center[1] - 40))
