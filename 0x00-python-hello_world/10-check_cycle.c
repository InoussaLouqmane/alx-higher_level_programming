#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * check_cycle - list to check
 * @list: the concerned list
 *
 * Return: 0 if has no cycle
 * 1 if it has cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *fox = list;

	if (list != NULL)
	{
		while ((tortoise->next) != NULL && (fox->next)->next != NULL)
		{
			tortoise = tortoise->next;
			fox = (fox->next)->next;
			if (fox == tortoise)
				return (1);
		}
	}
	return (0);
}
