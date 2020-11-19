# Visualising the results

# Note: I commented this out. You can do exactly this in a Jupyter Notebook!
# Save the predictions of the NN in a file, load it in a Jupyter Notebook and visualize like this

# plt.figure(figsize=(25,15), dpi=50, facecolor='w', edgecolor='k')
# ax = plt.gca()
# plt.plot(test_set, color = 'red', label = 'Real BTC Value')
# plt.plot(predicted_BTC_price, color = 'blue', label = 'Predicted BTC Price')
# plt.title('BTC Price Prediction', fontsize=20)
# df_test = df_test.reset_index()
# x=df_test.index
# labels = df_test['date']
# plt.xticks(x, labels, rotation = 'vertical')
# for tick in ax.xaxis.get_major_ticks():
# tick.label1.set_fontsize(10)
# for tick in ax.yaxis.get_major_ticks():
# tick.label1.set_fontsize(10)
# plt.xlabel('Time', fontsize=10)
# plt.ylabel('BTC Price(USD)', fontsize=20)
# plt.legend(loc=2, prop={'size': 25})
# plt.show()
