from dependency_injector import containers, providers

from kanban_board.repo.board import KanbanBoardRepoImpl
from kanban_board.services.board.create_board import CreateKanbanBoardCommandImpl

from users.repo.token import TokenRepoImpl
from users.repo.user import UserRepoImpl
from users.services.user.create_user import CreateUserCommandImpl
from users.services.user.login_user import LoginUserCommandImpl
from users.services.user.tokens_service import TokensServiceImpl


class Container(containers.DeclarativeContainer):
    # users
    user_repo = providers.Singleton(UserRepoImpl)
    token_repo = providers.Singleton(TokenRepoImpl)

    create_user = providers.Singleton(
        CreateUserCommandImpl,
        repo=user_repo
    )
    tokens_service = providers.Singleton(
        TokensServiceImpl,
        repo=token_repo
    )
    login_user = providers.Singleton(
        LoginUserCommandImpl,
        repo=user_repo,
        tokens_service=tokens_service
    )

    # board
    board_repo = providers.Singleton(KanbanBoardRepoImpl)

    create_board = providers.Singleton(
        CreateKanbanBoardCommandImpl,
        repo=board_repo
    )
