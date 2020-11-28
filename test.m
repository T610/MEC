y = linspace(1,10,1000)

%plot(x,gppdf(x,-.4,1),'-', x,gppdf(x,0,1),'-', x,gppdf(x,2,1),'-');
%y = [1,2,3,5]

threshold = 0
res = gpd( y,threshold )
plot(1,1)
 [length,r] = size(xi);
saveas(gcf,['.\gpd\',num2str(length),'.png'])
%title = [num2str(size(y))];
%saveas(gcf,title, 'png')
    




