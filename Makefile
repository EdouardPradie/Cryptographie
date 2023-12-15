##
## EPITECH PROJECT, 2023
## Crypto
## File description:
## Makefile
##

SRC		=	src/main

NAME	=	mypgp

all:	$(NAME)

$(NAME):
	cp $(SRC) $(NAME)

clean:
	@echo "project cleaning is in process [...]"

fclean:	clean
	$(RM) $(NAME)
	$(RM) ../$(NAME)

re:	fclean all

.PHONY: all clean fclean re
