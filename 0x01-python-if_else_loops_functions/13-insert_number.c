#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - insert a node in
 * sorted list
 * @head: head of list
 * @number: content of list
 *
 * Return: adress of new node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *searcher = *head;
	int trouver = 0;
	
	if (new_node == NULL || *head == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (searcher->next != NULL)
		{
			if ((searcher->next->n) > number)
			{
				new_node->next = searcher->next;
				searcher->next = new_node;
				trouver = 1;
				break;
			}
			searcher = searcher->next;
		}
		if (trouver == 0)
		{
			new_node->next = NULL;
			searcher->next = new_node;
		}
	}
	return (new_node);
}
