#include "lists.h"

/**
 * check_cycle - check if a cycle exist in a linked list
 * @list: linked list to check
 * Return: Returns (1) if cycle exit in the list, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
