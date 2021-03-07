#***(1)Returns all customers from customer table
customers = Customer.objects.all()

#(2)Returns first customer in table
firstCustomer = Customer.objects.first()

#(3)Returns last customer in table
lastCustomer = Customer.objects.last()

#(4)Returns single customer by name
customerByName = Customer.objects.get(name='Peter Piper')

#***(5)Returns single customer by name
customerById = Customer.objects.get(id=4)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#(7)***Returns orders customer name: (Query parent model values)
order = Order.objects.first() 
parentName = order.customer.name


'''
(11)Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database?
  
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''




#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()