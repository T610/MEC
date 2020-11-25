

function res = gpd(y,threshold )
[F,xi] = ecdf(y);
paramEsts = gpfit(y);
kHat      = paramEsts(1);
sigmaHat = paramEsts(2);

yi = gpcdf(xi,kHat,sigmaHat);
plot(xi,yi,'r-');
hold on;
%stairs(xi,F,'r');
hold on;

for  i=2:size(xi)

     if (xi(i-1) <= threshold  )  & ( threshold  <  xi(i) ) 
        [k,b] = forkb(xi(i-1),yi(i-1),xi(i),yi(i))
        probability = k*threshold + b
        break;
     end
end

plot(target,probability,'o')

function [k,b] = forkb(x1,y1,x2,y2)
    k = (y2-y1)/(x2-x1);
    b = y1 - x1*k;

end


res = [kHat,sigmaHat ,probability] ;
end
