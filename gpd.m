
function res = gpd(y,threshold )
[F,xi] = ecdf(y);
paramEsts = gpfit(y);
kHat      = paramEsts(1);
sigmaHat = paramEsts(2);

yi = gpcdf(xi,kHat,sigmaHat);
plot(xi,yi,'r-');
hold on;
stairs(xi,F,'b');
hold on;
probability = 1;
if xi(1) <=  threshold   &  threshold < xi( size(xi)  )
    for  i=2:size(xi)
    
     if (xi(i-1) <= threshold  )  & ( threshold  <  xi(i) ) 
        [k,b] = forkb(xi(i-1),yi(i-1),xi(i),yi(i))
        probability = k*threshold + b;
        break;
     end
    end
end
%plot(threshold,out,'o')
%hold on



res = [kHat,sigmaHat ,probability] ;
end

function [k,b] = forkb(x1,y1,x2,y2)
    k = (y2-y1)/(x2-x1);
    b = y1 - x1*k;

end
