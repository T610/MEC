x = linspace(0,10,1000)

%plot(x,gppdf(x,-.4,1),'-', x,gppdf(x,0,1),'-', x,gppdf(x,2,1),'-');
y = [1,2,3,5]


plot(x,gppdf(x,-.4,1))

gpd(y)
%cdfplot(x)